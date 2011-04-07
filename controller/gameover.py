import cocos

class GameOverController(cocos.layer.Layer):
	is_event_handler = True

	def __init__(self, model):
		super(GameOverController, self).__init__()
		self.model = model
