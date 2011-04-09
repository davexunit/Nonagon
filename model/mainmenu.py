import pyglet

class MainMenuModel(pyglet.event.EventDispatcher):
	"""Holds state for the Main Menu scene.
	"""
	def __init__(self):
		super(MainMenuModel, self).__init__()
		self.player = pyglet.media.Player()
		self.player.eos_action = pyglet.media.Player.EOS_LOOP
		self.music = pyglet.resource.media('Intro.mp3')
		self.player.queue(self.music)
