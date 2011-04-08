import cocos

class VictoryController(cocos.layer.Layer):
	is_event_handler = True

	def __init__(self, model):
		super(VictoryController, self).__init__()
		self.model = model
	
	def on_key_press(self, symbol, modifiers):
		# Pop scene when any key is pressed
		cocos.director.director.pop()
