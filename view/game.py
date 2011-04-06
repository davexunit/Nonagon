import cocos

class GameView(cocos.layer.ColorLayer):
	def __init__(self, model):
		super(GameView, self).__init__(255, 255, 255, 255)
		self.model = model

		self.add(self.model.testpoly)
		self.add(self.model.player)
