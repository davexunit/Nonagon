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
		self.rotate_ccw = key.Z
		self.rotate_cw = key.X
		self.flip_l = key.C
		self.flip_r = key.V
		self.fire = key.SPACE

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
			if self.last_transf != self.rotate_ccw:
				self.last_transf = self.rotate_ccw
				self.model.fire_player_bullet(RotateCCWBullet())
		elif symbol == self.rotate_cw:
			if self.last_transf != self.rotate_cw:
				self.last_transf = self.rotate_cw
				self.model.fire_player_bullet(RotateCWBullet())
		elif symbol == self.flip_l:
			if self.last_transf != self.flip_l:
				self.last_transf = self.flip_l
				self.model.fire_player_bullet(FlipLeftBullet())
		elif symbol == self.flip_r:
			if self.last_transf != self.flip_r:
				self.last_transf = self.flip_r
				self.model.fire_player_bullet(FlipRightBullet())
		elif symbol == self.fire:
			self.model.fire_player_bullet(KillBullet())
	
	def on_key_release(self, symbol, modifiers):
		if symbol == key.LEFT:
			self.model.player.stop_move(Player.MOVE_LEFT)
		elif symbol == key.RIGHT:
			self.model.player.stop_move(Player.MOVE_RIGHT)
		elif symbol == key.UP:
			self.model.player.stop_move(Player.MOVE_UP)
		elif symbol == key.DOWN:
			self.model.player.stop_move(Player.MOVE_DOWN)
	
	def step(self, dt):
		self.model.step(dt)
