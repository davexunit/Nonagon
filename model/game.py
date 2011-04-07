import pyglet
from pyglet.gl import *
import cocos
import math
import random

class GameModel(pyglet.event.EventDispatcher):
	def __init__(self):
		super(GameModel, self).__init__()
		# Testing out the polygon class.
		self.testpoly = EnemyPolygon(5)
		self.testpoly.position = 200, 200
		self.testpolys = cocos.cocosnode.CocosNode()
		
		# Just testing all the different enemy types
		for v in range(3, 9):
			poly = EnemyPolygon(v)
			poly.position = (v - 2) * 100, 500
			self.testpolys.add(poly)
			
		# Just a test to try out operations
		def stuff():
			self.testpoly.rotate_cw()
			#self.testpoly.rotate_ccw()
			#self.testpoly.flip_l()
			#self.testpoly.flip_r()
		self.testpoly.do((cocos.actions.Delay(1) + cocos.actions.CallFunc(stuff)) * 30)

		# Add the player
		self.player = Player()
		self.player.position = 400, 300
		
		# Node for player bullets
		self.player_bullets = cocos.batch.BatchNode()
	
	def step(self, dt):
		"""Called every frame, this method updates objects that have time dependent calculations to perform.
		"""
		self.player.step(dt)
		for b in self.player_bullets.children:
			b[1].step(dt)

class Bullet(cocos.sprite.Sprite):
	"""Provides the functionality to create differing bullet types by using event handlers.
	"""
	def __init__(self, image_file, dx=0, dy=500):
		"""dx and dy parameters set the bullet speed and vector.
		"""
		super(Bullet, self).__init__(image_file)
		self.dx = dx
		self.dy = dy
	
	def step(self, dt):
		self.x += self.dx * dt
		self.y += self.dy * dt

	def on_hit(self, entity):
		"""Hit event handler.
		Customize this to do what you want the bullet to do.
		"""
		pass

class RotateCWBullet(Bullet):
	"""Bullet that will rotate an enemy's kill vertex one 'step' clockwise.
	"""
	def __init__(self):
		super(RotateCWBullet, self).__init__('rotate_cw_bullet.png')
	
	def on_hit(self, entity):
		entity.rotate_cw()

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
	"""Our polygonal adversary.
	"""
	def __init__(self, num_vertices):
		#super(EnemyPolygon, self).__init__()
		cocos.cocosnode.CocosNode.__init__(self)
		Movable.__init__(self, 400)
		self.num_vertices = num_vertices
		# The more vertices, the bigger the polygon
		self.increment = 5
		self.base_size = 10
		self.radius = self.base_size + self.num_vertices * self.increment
		# Sprites that give a visual cue as to whether the kill vertex is exposed or not.
		self.no = cocos.sprite.Sprite('no.png')
		self.yes = cocos.sprite.Sprite('yes.png')
		# Enemy sprite
		# TODO: This will be customized on a per-enemy basis
		self.sprite = cocos.sprite.Sprite('enemy.png')
		self.add(self.sprite)
		
		# Assign the kill vertex to a non-downward vertex. The polygon's
		# downward vertex is zero, and the rest are numbered
		# incrementally counter-clockwise from the downward vertex.
		self.kill_vertex = random.randrange(0, num_vertices)
		self.update_sprites()

	def update_sprites(self):
		"""Sets the correct sprites based upon the kill vertex.
		"""
		if self.kill_vertex == 0:
			# This is a bit of a hack... it's just not pretty. It works, though.
			# Catch element not found exceptions
			try:
				self.remove(self.no)
			except:
				pass
			self.add(self.yes)
			angle = 2 * math.pi * self.kill_vertex / self.num_vertices - math.pi / 2
			self.yes.position = self.radius * math.cos(angle), self.radius * math.sin(angle)
		else:
			try:
				self.remove(self.yes)
			except:
				pass
			self.add(self.no)
			angle = 2 * math.pi * self.kill_vertex / self.num_vertices - math.pi / 2
			self.no.position = self.radius * math.cos(angle), self.radius * math.sin(angle)

	# Rotate clockwise
	def rotate_cw(self):
		self.kill_vertex = (self.kill_vertex - 1) % self.num_vertices
		self.update_sprites()

	# Rotate counter-clockwise
	def rotate_ccw(self):
		self.kill_vertex = (self.kill_vertex + 1) % self.num_vertices
		self.update_sprites()

	# Flip about line of symmetry passing through the side directly
	# to the left of the downward vertex
	def flip_l(self):
		self.kill_vertex = (-self.kill_vertex - 1) % self.num_vertices
		self.update_sprites()

	# Flip about line of symmetry passing through the side directly
	# to the right of the downward vertex
	def flip_r(self):
		self.kill_vertex = (-self.kill_vertex + 1) % self.num_vertices
		self.update_sprites()

	# Need to work out the OpenGL/pyglet vertex buffer business here, but
	# here's a sketch for how we can draw the polygon and its
	# kill vertex:
	def draw(self):
		glPushMatrix()
		self.transform()
		# Draw polygon
		#glColor3f(0.0, 0.0, 0.5) # Dark blue color
		if self.kill_vertex != 0:
			glColor3f(1.0, 0.0, 0.0) # red color
		else:
			glColor3f(0.0, 1.0, 0.0)
		glLineWidth(4)
		glEnable(GL_LINE_SMOOTH)
		# Construct polygon by its vertices, starting with the
		# downward vertex and working counter-clockwise
		# TODO: Put this stuff in a vertex buffer
		glBegin(GL_LINE_LOOP)
		for i in range(self.num_vertices):
			angle = 2 * math.pi * i / self.num_vertices - math.pi / 2
			glVertex2f(self.radius * math.cos(angle), self.radius * math.sin(angle))
		glEnd()

		# Draw kill vertex indicator
		# TODO: This should be a child node
		'''kv_ind_size = 5 # Size of kill vertex indicator
		glColor3f(1.0, 0.0, 0.0) # Red color
		angle = 2 * math.pi * self.kill_vertex / self.num_vertices - math.pi / 2
		kv_ind_x = self.radius * math.cos(angle)
		kv_ind_y = self.radius * math.sin(angle)
		glPushMatrix()
		glTranslatef(kv_ind_x, kv_ind_y, 0)
		glBegin(GL_QUADS)
		glVertex2f(-kv_ind_size, -kv_ind_size)
		glVertex2f(-kv_ind_size, kv_ind_size)
		glVertex2f(kv_ind_size, kv_ind_size)
		glVertex2f(kv_ind_size, -kv_ind_size)
		glEnd()
		glPopMatrix()'''
		glPopMatrix()
	
