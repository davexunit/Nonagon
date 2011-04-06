import cocos
from cocos.director import director
from cocos.menu import *

class MainMenuView(cocos.layer.Layer):
	"""Draws the main menu scene.
	Add a better description please.
	"""
	def __init__(self, model):
		"""Creates the MainMenu layer using the given model.
		"""
		super(MainMenuView, self).__init__()
		self.model = model
		# Our super awesome logo
		self.logo = cocos.sprite.Sprite('logo.png')
		w, h = director.get_window_size()
		self.logo.position = w / 2, h - 10 - self.logo.height / 2
		# Add our menu
		self.add(MainMenu())
		self.add(self.logo)

class MainMenu(Menu):
	"""Defines the style and options available in the main menu.
	It's ugly that this is in the view module because we define some game logic here based upon what option the user chooses but there's not much we can do about that.
	"""
	def __init__(self):
		super(MainMenu, self).__init__('')
		# Create the menu items
		items = []
		items.append(MenuItem('Play', self.on_play))
		items.append(MenuItem('Options', self.on_options))
		items.append(MenuItem('Quit', self.on_quit))

		# Finalize the menu
		self.create_menu(items)
	
	def on_play(self):
		pass
	
	def on_options(self):
		pass
	
	def on_quit(self):
		# Pop this scene off of the scene stack.
		# This should end the program because there should be no other scenes under the main menu in the stack.
		director.pop()
