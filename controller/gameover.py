import cocos
from cocos.scenes.transitions import *

class GameOverController(cocos.layer.Layer):
	is_event_handler = True

	def __init__(self, model):
		super(GameOverController, self).__init__()
		self.model = model
	
	def on_key_press(self, symbol, modifiers):
		cocos.director.director.pop()
