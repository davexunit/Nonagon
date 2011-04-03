import cocos

class MainMenuController(cocos.layer.Layer):
	"""Handles user input for the main menu scene.
	There is a small caveat here in that user input for the menu itself is NOT handled here as it is included within the cocos.menu.Menu class.
	There is no easy, elegant way  to separate the logic from the representation of the menu. It's not a big deal so don't worry about it. :]
	"""
	# This tells cocos that we want to receive events
	is_event_handler=True

	def __init__(self, model):
		super(MainMenuController, self).__init__()
		self.model = model
