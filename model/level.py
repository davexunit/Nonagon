import pyglet
import cocos
from cocos.path import Bezier
import game

class Wave(cocos.cocosnode.CocosNode, pyglet.event.EventDispatcher):
	"""Defines the type of enemies that appear in a level and defines their behavior.
	"""
	def __init__(self, enemy_list):
		"""enemy_list is a list of (num_vertices, action) pairs.
		"""
		super(Wave, self).__init__()
		w,h = cocos.director.director.get_window_size()
		for i, enemy_tuple in enumerate(enemy_list):
			vertex_count, enemy_action = enemy_tuple
			enemy = game.EnemyPolygon(vertex_count)
			enemy.push_handlers(self)
			enemy.position =  w/len(enemy_list)*(i+0.5), h-100
			self.add(enemy)
			if enemy_action != None:
				enemy.do(enemy_action)
			else:
				path = create_enemy_path(enemy, enemy.x + 100, enemy.y - 300, BEND_UP)
				action = cocos.actions.Bezier(path, 5)
				enemy.do(action)

	def on_enemy_death(self, entity):
		entity.kill()
		# Check if wave is empty
		if not self.get_children():
			self.dispatch_event('on_wave_complete', self)

Wave.register_event_type('on_wave_complete')


class Level(cocos.cocosnode.CocosNode):
	"""Contains many waves of enemies that the player must defeat.
	"""
	def __init__(self, wave_list):
		super(Level,self).__init__()
		# For testing purposes, only load first wave in wave_list
		self.current_wave = wave_list[0]
		self.current_wave.push_handlers(self)
		self.add(self.current_wave)

	def on_wave_complete(self, wave):
		print "Wave complete!"
		
				
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

