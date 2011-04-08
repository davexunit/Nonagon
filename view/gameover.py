import cocos

class GameOverView(cocos.layer.Layer):
	def __init__(self, model):
		super(GameOverView, self).__init__()
		self.model = model
		self.add(self.model.label)
		self.add(self.model.label2)
