import cocos

class GameOverView(cocos.layer.Layer):
	def __init__(self, model):
		super(GameOverView, self).__init__()
		self.model = model
		w, h = cocos.director.director.get_window_size()
		self.label = cocos.text.Label('GAME OVER', font_name='Orbitron', font_size=64, anchor_x='center', anchor_y='center')
		self.label.position = w / 2, h / 2
		self.add(self.label)
