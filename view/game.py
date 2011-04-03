import cocos

class GameView(cocos.layer.Layer):
	def __init__(self, model):
		super(GameView, self).__init__()
		self.model = model
