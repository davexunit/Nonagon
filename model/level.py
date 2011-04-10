import pyglet
import cocos
from cocos.actions import *
import game
from collections import deque

class WaveEnemy(object):
	"""This class contains the components that will make up an enemy in the wave.
	"""
	def __init__(self, num_vertices, kill_vertex, action_callback, weapon_callback):
		self.num_vertices = num_vertices
		self.kill_vertex = kill_vertex
		self.action_callback = action_callback
		self.weapon_callback = weapon_callback
	
	def make_enemy(self):
		enemy = game.EnemyPolygon(self.num_vertices, self.kill_vertex)
		enemy.weapon = self.weapon_callback(enemy)
		def do_action(dt):
			enemy.do(self.action_callback(enemy))
		# This is a hack to start the action on the next frame so that the action is set AFTER the layout strategy has positioned the enemies
		pyglet.clock.schedule_once(do_action, 0)
		# Fade in because it looks nicer than something just popping into existance
		enemy.do(FadeIn(2))
		return enemy

class WaveBoss(object):
	"""This class is a factory for making THE NONAGON!!!1!1!one!
	"""
	def __init__(self, action_callback, weapon_callback):
		self.action_callback = action_callback
		self.weapon_callback = weapon_callback
		
	def make_enemy(self):
		enemy = game.Nonagon()
		enemy.weapon = self.weapon_callback(enemy)
		def do_action(dt):
			enemy.do(self.action_callback(enemy))
		# This is a hack to start the action on the next frame so that the action is set AFTER the layout strategy has positioned the enemies
		pyglet.clock.schedule_once(do_action, 0)
		# Fade in because it looks nicer than something just popping into existance
		enemy.do(FadeIn(2))
		return enemy

def horizontalLayout(y):
	"""Accepts a list of enemies and places them in a horizontal line
	"""
	def horizontalLayoutFunc(enemies):
		w, h = cocos.director.director.get_window_size()
		l = len(enemies)
		for i, e in enumerate(enemies):
			e.position = (w / l) * (i + 0.25), y
	return horizontalLayoutFunc
		
class Wave(cocos.cocosnode.CocosNode, pyglet.event.EventDispatcher):
	"""Defines the type of enemies that appear in a level and their behavior.
	"""
	def __init__(self, layout_strategy, enemy_list):
		"""enemy_list is a list of (num_vertices, action) pairs.
		"""
		super(Wave, self).__init__()
		self.layout_strategy = layout_strategy
		self.enemy_list = list(enemy_list)

	def pause(self):
		super(Wave, self).pause()
		for enemy in self.get_children():
			enemy.pause()

	def pause_scheduler(self):
		super(Wave, self).pause_scheduler()
		for enemy in self.get_children():
			enemy.pause_scheduler()

	def resume(self):
		super(Wave, self).resume()
		for enemy in self.get_children():
			enemy.resume()

	def resume_scheduler(self):
		super(Wave, self).resume_scheduler()
		for enemy in self.get_children():
			enemy.resume_scheduler()
	
	def create_wave(self):
		# Create enemies from given data
		for e in self.enemy_list:
			enemy = e.make_enemy()
			enemy.push_handlers(self)
			self.add(enemy)
		# Position enemies
		self.layout_strategy(self.get_children())

	def on_enemy_death(self, enemy):
		self.remove(enemy)
		# Check if wave is empty
		if not self.get_children():
			self.dispatch_event('on_wave_complete', self)

Wave.register_event_type('on_wave_complete')

class Level(cocos.cocosnode.CocosNode, pyglet.event.EventDispatcher):
	"""Contains many waves of enemies that the player must defeat.
	"""
	def __init__(self, wave_list, music_file):
		super(Level,self).__init__()
		# For testing purposes, only load first wave in wave_list
		self.wave_list = deque(wave_list)
		self.player = pyglet.media.Player()
		self.player.eos_action = pyglet.media.Player.EOS_LOOP
		self.music = pyglet.resource.media(music_file)
		self.player.queue(self.music)
		self.current_wave = None

	def pause(self):
		super(Level, self).pause()
		if self.current_wave != None:
			self.current_wave.pause()

	def pause_scheduler(self):
		super(Level, self).pause_scheduler()
		if self.current_wave != None:
			self.current_wave.pause_scheduler()

	def resume(self):
		super(Level, self).resume()
		if self.current_wave != None:
			self.current_wave.resume()

	def resume_scheduler(self):
		super(Level, self).resume_scheduler()
		if self.current_wave != None:
			self.current_wave.resume_scheduler()
	
	def next_wave(self):
		if not self.player.playing:
			self.player.play()
		# Dispatch level complete event and return when wave is finished.
		if len(self.wave_list) == 0:
			self.dispatch_event('on_level_complete')
			self.player.pause()
			return

		# Pop wave off of list
		self.current_wave = self.wave_list.popleft()
		# Initialize
		self.current_wave.create_wave()
		# Dispatch new wave event
		self.dispatch_event('on_new_wave', self.current_wave)
		# Push handlers
		self.current_wave.push_handlers(self)
		# Add to node
		self.add(self.current_wave)

	def on_wave_complete(self, wave):
		self.next_wave()

Level.register_event_type('on_level_complete')
Level.register_event_type('on_new_wave')
				
BEND_NONE = 0
BEND_DOWN = 1
BEND_UP = 2
def create_enemy_path(enemy, x_dest, y_dest, bend):
	"""Creates a Bezier path for an enemy polygon. The path extends from
	the enemy's current position to (x_dest, y_dest). bend determines
	the basic curvature of the path.
	"""
	rel_start = (0,0)
	rel_end = (x_dest-enemy.x, y_dest-enemy.y)

	rel_start_handle = rel_start
	rel_end_handle = rel_end

	# Adjust bend, depending on whether ship is moving up or down
	if y_dest < enemy.y:
		bend = (bend * 2) % 3

	if bend == BEND_UP:
		rel_start_handle = (rel_start[0], rel_start[1] + rel_end[1])
		rel_end_handle = (rel_end[0] - rel_start[0], rel_end[1])
	elif bend == BEND_DOWN:
		rel_start_handle = (rel_start[0] + rel_end[0], rel_start[1])
		rel_end_handle = (rel_end[0] , rel_end[1] - rel_start[0])

	path = cocos.path.Bezier(rel_start, rel_end, rel_start_handle, rel_end_handle)

	return path

def get_levels():
	"""Woo hoo we're hardcoding all of our levels here!
	"""
	levels = deque()
	def make_action(enemy):
		path = create_enemy_path(enemy, enemy.x + 100, enemy.y - 150, BEND_UP)
		action = Bezier(path, 5)
		return Repeat(action + MoveBy((-100, 150)))
	def make_basic_weapon(enemy):
		return game.BasicEnemyWeapon(enemy, 3, .3, 2)
	def make_fan_weapon(enemy):
		return game.FanEnemyWeapon(enemy, 3, .1, 3)
	def make_sweep_weapon(enemy):
		return game.SweepEnemyWeapon(enemy, 3, .1, 3)
	enemy1 = WaveEnemy(3, 1, make_action, make_basic_weapon)
	enemy2 = WaveEnemy(5, 3, make_action, make_sweep_weapon)
	nonagon = WaveBoss(make_action, make_fan_weapon)
	wave0 = Wave(horizontalLayout(600), [enemy1, enemy1, enemy1, enemy1])
	wave1 = Wave(horizontalLayout(500), [enemy1, enemy2, enemy1, enemy2])
	wave2 = Wave(horizontalLayout(400), [enemy2, enemy2, enemy2, enemy2])
	wave3 = Wave(horizontalLayout(500), [nonagon])
	level1 = Level([wave0, wave1, wave2], 'Level1.mp3')
	level2 = Level([wave3], 'Boss.mp3')
	levels.append(level1)
	levels.append(level2)

	return levels
