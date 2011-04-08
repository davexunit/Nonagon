import pyglet
import cocos

class GameOverModel(pyglet.event.EventDispatcher):
	def __init__(self, score):
		super(GameOverModel, self).__init__()
		w, h = cocos.director.director.get_window_size()
		self.label = cocos.text.Label('GAME OVER', font_name='Orbitron', font_size=64, anchor_x='center', anchor_y='center')
		self.label.position = w / 2, h / 2
		self.label2 = cocos.text.Label('Score: %d' % score, font_name='Orbitron', font_size=32, anchor_x='center', anchor_y='center')
		self.label2.position = w / 2, h / 2 - 100
