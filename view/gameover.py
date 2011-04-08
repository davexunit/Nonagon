import cocos

class GameOverView(cocos.layer.Layer):
	def __init__(self, model):
		super(GameOverView, self).__init__()
		self.model = model
		w, h = cocos.director.director.get_window_size()
		self.message= cocos.text.Label(self.model.message, font_name='Orbitron', font_size=64, anchor_x='center', anchor_y='center')
		self.message.position = w / 2, h / 2
		self.score = cocos.text.Label('Score: %d' % self.model.score, font_name='Orbitron', font_size=32, anchor_x='center', anchor_y='center')
		self.score.position = w / 2, h / 2 - 100
		self.add(self.message)
		self.add(self.score)
