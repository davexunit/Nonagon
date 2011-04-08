import cocos
from pyglet.window import key
from model.game import *

class GameController(cocos.layer.Layer):
	is_event_handler = True

	def __init__(self, model):
		super(GameController, self).__init__()
		self.model = model
		self.schedule(self.step)
		
		# Weapon key assignments; QWERTY for now
		self.rotate_cw = key.A
		self.rotate_ccw = key.S
		self.flip_l = key.D
		self.flip_r = key.F
		self.fire_key = key.SPACE

		self.last_transf = ''

	def on_key_press(self, symbol, modifiers):
		if symbol == key.LEFT:
			self.model.player.move(Player.MOVE_LEFT)
		elif symbol == key.RIGHT:
			self.model.player.move(Player.MOVE_RIGHT)
		elif symbol == key.UP:
			self.model.player.move(Player.MOVE_UP)
		elif symbol == key.DOWN:
			self.model.player.move(Player.MOVE_DOWN)
		elif symbol == self.rotate_ccw:
			self.model.player.fire(RotateCCWBullet())
		elif symbol == self.rotate_cw:
			self.model.player.fire(RotateCWBullet())
		elif symbol == self.flip_l:
			self.model.player.fire(FlipLeftBullet())
		elif symbol == self.flip_r:
			self.model.player.fire(FlipRightBullet())
		elif symbol == self.fire_key:
			self.start_fire()
	
	def on_key_release(self, symbol, modifiers):
		if symbol == key.LEFT:
			self.model.player.stop_move(Player.MOVE_LEFT)
		elif symbol == key.RIGHT:
			self.model.player.stop_move(Player.MOVE_RIGHT)
		elif symbol == key.UP:
			self.model.player.stop_move(Player.MOVE_UP)
		elif symbol == key.DOWN:
			self.model.player.stop_move(Player.MOVE_DOWN)
		elif symbol == self.fire_key:
			self.stop_fire()
	
	def start_fire(self):
		self.fire(0)
		self.model.player.schedule_interval(self.fire, .08)
	
	def stop_fire(self):
		self.model.player.unschedule(self.fire)
	
	def fire(self, dt):
		self.model.player.fire(KillBullet())
	
	def step(self, dt):
		self.model.step(dt)
