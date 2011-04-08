import pyglet
import cocos

class GameOverModel(pyglet.event.EventDispatcher):
	def __init__(self, score):
		super(GameOverModel, self).__init__()
		self.message = 'GAME OVER'
		self.score = score
