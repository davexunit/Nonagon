import cocos

class GameController(cocos.layer.Layer):
	def __init__(self, model):
		super(GameController, self).__init__()
		self.model = model
