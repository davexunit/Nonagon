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
		self.testpoly = EnemyPolygon(5, 100, 100)

class EnemyPolygon(cocos.cocosnode.CocosNode):
	def __init__(self, num_vertices, x_pos, y_pos):
		super(EnemyPolygon, self).__init__()
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
			glVertex3f(radius * math.cos(angle),
				   radius * math.sin(angle),
				   0)
		glEnd()

		# Draw kill vertex indicator
		kv_ind_size = 5 # Size of kill vertex indicator
		glColor3f(1.0, 0.0, 0.0) # Red color
		angle = 2 * math.pi * self.kill_vertex / self.num_vertices - math.pi / 2
		kv_ind_x = radius * math.cos(angle)
		kv_ind_y = radius * math.cos(angle)
		glBegin(GL_QUADS)
		glVertex2f(kv_ind_x, kv_ind_y)
		glVertex2f(kv_ind_x, kv_ind_y + kv_ind_size)
		glVertex2f(kv_ind_x + kv_ind_size, kv_ind_y + kv_ind_size)
		glVertex2f(kv_ind_x + kv_ind_size, kv_ind_y)
		glEnd()
		#glRect(kv_ind_x - kv_ind_size, kv_ind_y - kv_ind_size,
		#	   kv_ind_x + kv_ind_size, kv_ind_y + kv_ind_size)
		glPopMatrix()
	
