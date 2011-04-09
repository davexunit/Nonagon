import random
import pyglet
import cocos
from cocos.director import director

class MainMenuView(cocos.layer.ColorLayer):
	"""Draws the main menu scene.
	Add a better description please.
	"""
	def __init__(self, model):
		"""Creates the MainMenu layer using the given model.
		"""
		super(MainMenuView, self).__init__(255, 255, 255, 255)
		self.model = model
		# Our super awesome logo
		self.logo = cocos.sprite.Sprite('logo.png')
		w, h = director.get_window_size()
		# Position our logo somewhere nice.
		self.logo.position = w / 2, h - 100 - self.logo.height / 2
		# Make some sprites float around the screen.
		self.batch = cocos.batch.BatchNode()
		images = ['rotate_cw.png', 'nonagon.png']
		
		# Create 30 sprites, choosing randomly between the 2 images specified.
		for i in range(30):
			sprite = cocos.sprite.Sprite(images[random.randint(0, 1)])
			sprite.position = random.randint(0, w), random.randint(0, h)
			sprite.velocity = random.randint(150, 300), random.randint(150, 300)
			sprite.do(cocos.actions.move_actions.WrappedMove(w, h))
			self.batch.add(sprite)

		# Add our menu
		self.add(self.batch)
		self.add(self.model.multiplex)
		self.add(self.logo)

