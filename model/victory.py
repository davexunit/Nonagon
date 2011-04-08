import pyglet

class VictoryModel(pyglet.event.EventDispatcher):
	def __init__(self, score):
		super(VictoryModel, self).__init__()
		self.message = 'You have defeated the Nonagon!'
		self.sub_message = 'The world is now free from regular polygons!'
		self.score = score
