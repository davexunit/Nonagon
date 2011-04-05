import pyglet
from pyglet.gl import *
import math
import random

class GameModel(pyglet.event.EventDispatcher):
	def __init__(self):
		super(GameModel, self).__init__()

class EnemyPolygon(object):
	def __init__(self, num_vertices, x_pos, y_pos):
		self.num_vertices = num_vertices
		self.x_pos = x_pos
		self.y_pos = y_pos
		
		# Assign the kill vertex to a non-downward vertex. The polygon's
		# downward vertex is zero, and the rest are numbered
		# incrementally counter-clockwise from the downward vertex.
		self.kill_vertex = random.randrange(1, num_vertices)

		# Rotate clockwise
		def rotate_cw():
			self.kill_vertex = (self.kill_vertex - 1) % self.num_vertices

		# Rotate counter-clockwise
		def rotate_ccw():
			self.kill_vertex = (self.kill_vertex + 1) % self.num_vertices

		# Flip about line of symmetry passing through the side directly
		# to the left of the downward vertex
		def flip_l():
			self.kill_vertex = (-self.kill_vertex - 1) % self.num_vertices

		# Flip about line of symmetry passing through the side directly
		# to the right of the downward vertex
		def flip_r():
			self.kill_vertex = (-self.kill_vertex + 1) % self.num_vertices

		# Need to work out the OpenGL/pyglet vertex buffer business here, but
		# here's a sketch for how we can draw the polygon and its
		# kill vertex:
		def draw():
			# Draw polygon
			radius = 100 # 'Radius' of polygon
			glColor3f(0.0, 0.0, 0.5) # Dark blue color
			# Construct polygon by its vertices, starting with the
			# downward vertex and working counter-clockwise
			glBegin()
			for i in range(self.num_vertices):
				angle = 2*math.pi * i/self.num_vertices - math.pi/2
				glVertex3f(radius * math.cos(angle) + x_pos,
					   radius * math.sin(angle) + y_pos,
					   0)
			glEnd()
			
			# Draw kill vertex indicator
			kv_ind_size = 5 # Size of kill vertex indicator
			glColor3f(1.0, 0.0, 0.0) # Red color
			angle = 2*math.pi * self.kill_vertex/self.num_vertices - math.pi/2
			kv_ind_x = radius*math.cos(angle) + x_pos
			kv_ind_y = radius*math.cos(angle) + y_pos
			glRect(kv_ind_x - kv_ind_size, kv_ind_y - kv_ind_size,
			       kv_ind_x + kv_ind_size, kv_ind_y + kv_ind_size)
			
		
		
