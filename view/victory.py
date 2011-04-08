import cocos

class VictoryView(cocos.layer.Layer):
	def __init__(self, model):
		super(VictoryView, self).__init__()
		self.model = model
		w, h = cocos.director.director.get_window_size()
		self.message = cocos.text.Label(self.model.message, font_name='Orbitron', font_size=32, anchor_x='center', anchor_y='center')
		self.message.position = w/2, h/2
		self.sub_message = cocos.text.Label(self.model.sub_message, font_name='Orbitron', font_size=20, anchor_x='center', anchor_y='center')
		self.sub_message.position = w/2, h/2 - h/5
		self.score = cocos.text.Label('Final score: %d' % self.model.score, font_name='Orbitron', font_size=20, anchor_x='center', anchor_y='center')
		self.score.position = w/2, h/2 - h/3

		self.add(self.message)
		self.add(self.sub_message)
		self.add(self.score)
		
