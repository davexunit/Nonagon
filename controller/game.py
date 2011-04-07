import cocos
from pyglet.window import key
from model.game import Movable, RotateCWBullet

class GameController(cocos.layer.Layer):
	is_event_handler = True

	def __init__(self, model):
		super(GameController, self).__init__()
		self.model = model
		self.schedule(self.step)
		
		# Weapon key assignments; QWERTY for now
		self.rotate_ccw = key.Z
		self.rotate_cw = key.X
		self.flip_l = key.C
		self.flip_r = key.V
		self.fire = key.SPACE

		self.last_transf = ''

	def on_key_press(self, symbol, modifiers):
		if symbol == key.LEFT:
			self.model.player.move(Movable.MOVE_LEFT)
		elif symbol == key.RIGHT:
			self.model.player.move(Movable.MOVE_RIGHT)
		elif symbol == key.UP:
			self.model.player.move(Movable.MOVE_UP)
		elif symbol == key.DOWN:
			self.model.player.move(Movable.MOVE_DOWN)
		elif symbol == self.rotate_ccw:
			if self.last_transf != self.rotate_ccw:
				self.last_transf = self.rotate_ccw
				print 'rotate ccw'
		elif symbol == self.rotate_cw:
			if self.last_transf != self.rotate_cw:
				self.last_transf = self.rotate_cw
				bullet = RotateCWBullet()
				bullet.position = self.model.player.position
				self.model.player_bullets.add(bullet)
		elif symbol == self.flip_l:
			if self.last_transf != self.flip_l:
				self.last_transf = self.flip_l
				print 'flip l'
		elif symbol == self.flip_r:
			if self.last_transf != self.flip_r:
				self.last_transf = self.flip_r
				print 'flip r'
		elif symbol == self.fire:
			print 'fire'
				
	
	def on_key_release(self, symbol, modifiers):
		if symbol == key.LEFT:
			self.model.player.stop_move(Movable.MOVE_LEFT)
		elif symbol == key.RIGHT:
			self.model.player.stop_move(Movable.MOVE_RIGHT)
		elif symbol == key.UP:
			self.model.player.stop_move(Movable.MOVE_UP)
		elif symbol == key.DOWN:
			self.model.player.stop_move(Movable.MOVE_DOWN)
	
	def step(self, dt):
		self.model.step(dt)
