import pyglet
from pyglet.gl import *
import cocos
import math
import random

class GameModel(pyglet.event.EventDispatcher):
	def __init__(self):
		super(GameModel, self).__init__()
		# Create a batch for faster rendering awesomeness.
		self.batch = cocos.batch.BatchNode()
		# Testing out the polygon class.
		self.testpoly = EnemyPolygon(5, 200, 200)
		def stuff():
			#self.testpoly.rotate_cw()
			#self.testpoly.rotate_ccw()
			#self.testpoly.flip_l()
			self.testpoly.flip_r()
		self.testpoly.do((cocos.actions.Delay(1) + cocos.actions.CallFunc(stuff)) * 10)
		self.player = Player()
		self.player.position = 400, 300
	
	def step(self, dt):
		"""Called every frame, this method updates objects that have time dependent calculations to perform.
		"""
		self.player.step(dt)

class Movable(object):
	""" Provides movement functionality for game objects.
	"""
	# Fuck yeah bit masks!
	MOVE_LEFT = 1
	MOVE_RIGHT = 2
	MOVE_UP = 4
	MOVE_DOWN = 8

	def __init__(self, speed):
		self.speed = speed
		self.move_mask = 0

	def move(self, direction):
		self.move_mask |= direction
	
	def stop_move(self, direction):
		self.move_mask &= ~direction

	def step(self, dt):
		dx = 0
		dy = 0

		if self.move_mask & self.MOVE_LEFT:
			dx = -self.speed * dt
		if self.move_mask & self.MOVE_RIGHT:
			dx = self.speed * dt
		if self.move_mask & self.MOVE_UP:
			dy = self.speed * dt
		if self.move_mask & self.MOVE_DOWN:
			dy = -self.speed * dt

		self.x += dx
		self.y += dy	

class Player(cocos.sprite.Sprite, Movable):
	"""Our courageous player!
	"""
	def __init__(self):
		cocos.sprite.Sprite.__init__(self, 'ship.png')
		Movable.__init__(self, 500)

class EnemyPolygon(cocos.cocosnode.CocosNode, Movable):
	"""Our polygon adversary.
	"""
	def __init__(self, num_vertices, x_pos, y_pos):
		#super(EnemyPolygon, self).__init__()
		cocos.cocosnode.CocosNode.__init__(self)
		Movable.__init__(self, 400)
		self.num_vertices = num_vertices
		self.x = x_pos
		self.y = y_pos
		
		# Assign the kill vertex to a non-downward vertex. The polygon's
		# downward vertex is zero, and the rest are numbered
		# incrementally counter-clockwise from the downward vertex.
		self.kill_vertex = random.randrange(1, num_vertices)

	# Rotate clockwise
	def rotate_cw(self):
		self.kill_vertex = (self.kill_vertex - 1) % self.num_vertices

	# Rotate counter-clockwise
	def rotate_ccw(self):
		self.kill_vertex = (self.kill_vertex + 1) % self.num_vertices

	# Flip about line of symmetry passing through the side directly
	# to the left of the downward vertex
	def flip_l(self):
		self.kill_vertex = (-self.kill_vertex - 1) % self.num_vertices

	# Flip about line of symmetry passing through the side directly
	# to the right of the downward vertex
	def flip_r(self):
		self.kill_vertex = (-self.kill_vertex + 1) % self.num_vertices

	# Need to work out the OpenGL/pyglet vertex buffer business here, but
	# here's a sketch for how we can draw the polygon and its
	# kill vertex:
	def draw(self):
		glPushMatrix()
		self.transform()
		# Draw polygon
		radius = 100 # 'Radius' of polygon
		glColor3f(0.0, 0.0, 0.5) # Dark blue color
		# Construct polygon by its vertices, starting with the
		# downward vertex and working counter-clockwise
		# TODO: Put this stuff in a vertex buffer
		glBegin(GL_LINE_LOOP)
		for i in range(self.num_vertices):
			angle = 2 * math.pi * i / self.num_vertices - math.pi / 2
			glVertex2f(radius * math.cos(angle), radius * math.sin(angle))
		glEnd()

		# Draw kill vertex indicator
		kv_ind_size = 5 # Size of kill vertex indicator
		glColor3f(1.0, 0.0, 0.0) # Red color
		angle = 2 * math.pi * self.kill_vertex / self.num_vertices - math.pi / 2
		kv_ind_x = radius * math.cos(angle)
		kv_ind_y = radius * math.sin(angle)
		glPushMatrix()
		glTranslatef(kv_ind_x, kv_ind_y, 0)
		glBegin(GL_QUADS)
		glVertex2f(-kv_ind_size, -kv_ind_size)
		glVertex2f(-kv_ind_size, kv_ind_size)
		glVertex2f(kv_ind_size, kv_ind_size)
		glVertex2f(kv_ind_size, -kv_ind_size)
		glEnd()
		glPopMatrix()
		#glRect(kv_ind_x - kv_ind_size, kv_ind_y - kv_ind_size,
		#	   kv_ind_x + kv_ind_size, kv_ind_y + kv_ind_size)
		glPopMatrix()
	
