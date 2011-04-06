import cocos
from pyglet.window import key
from model.game import Movable

class GameController(cocos.layer.Layer):
	is_event_handler = True

	def __init__(self, model):
		super(GameController, self).__init__()
		self.model = model
		self.schedule(self.step)

	def on_key_press(self, symbol, modifiers):
		if symbol == key.LEFT:
			self.model.player.move(Movable.MOVE_LEFT)
		elif symbol == key.RIGHT:
			self.model.player.move(Movable.MOVE_RIGHT)
		elif symbol == key.UP:
			self.model.player.move(Movable.MOVE_UP)
		elif symbol == key.DOWN:
			self.model.player.move(Movable.MOVE_DOWN)
	
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
