import pyglet
import cocos
from cocos.actions import *
from cocos.path import Bezier
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
		enemy.do(FadeIn(1))
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
	def __init__(self, wave_list):
		super(Level,self).__init__()
		# For testing purposes, only load first wave in wave_list
		self.wave_list = deque(wave_list)
	
	def next_wave(self):
		# Dispatch level complete event and return when wave is finished.
		if len(self.wave_list) == 0:
			self.dispatch_event('on_level_complete')
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

	path = Bezier(rel_start, rel_end, rel_start_handle, rel_end_handle)

	return path

