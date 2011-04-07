import random
import pyglet
import cocos
from cocos.director import director
from cocos.menu import *

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
		self.add(MainMenu())
		self.add(self.logo)

# This is a layout strategy function for the MainMenu class.
# This is copied from the cocos2d source code and modified to provide padding inbetween menu options.
def paddedVerticalLayout(padding):
	def betterVerticalLayout(menu):
		width, height = director.get_window_size()
		fo = pyglet.font.load(menu.font_item['font_name'], menu.font_item['font_size'])
		fo_height = int((fo.ascent - fo.descent) * 0.9) + padding

		if menu.menu_halign == CENTER:
			pos_x = width // 2
		elif menu.menu_halign == RIGHT:
			pos_x = width - menu.menu_hmargin
		elif menu.menu_halign == LEFT:
			pos_x = menu.menu_hmargin
		else:
			raise Exception("Invalid anchor_x value for menu")

		for idx,i in enumerate( menu.children):
			item = i[1]
			if menu.menu_valign == CENTER:
				pos_y = (height + (len(menu.children) - 2 * idx)
							 * fo_height - menu.title_height) * 0.5
			elif menu.menu_valign == TOP:
				pos_y = (height - ((idx + 0.8) * fo_height )
							 - menu.title_height - menu.menu_vmargin)
			elif menu.menu_valign == BOTTOM:
				pos_y = (0 + fo_height * (len(menu.children) - idx) +
							 menu.menu_vmargin)
			item.transform_anchor = (pos_x, pos_y)
			item.generateWidgets (pos_x, pos_y, menu.font_item,
								  menu.font_item_selected)
	
	return betterVerticalLayout

class MainMenu(Menu):
	"""Defines the style and options available in the main menu.
	It's ugly that this is in the view module because we define some game logic here based upon what option the user chooses but there's not much we can do about that.
	"""
	def __init__(self):
		super(MainMenu, self).__init__('')
		# Menu item font properties
		self.font_item['font_name'] = 'Orbitron'
		#self.font_item['font_size'] = 24
		self.font_item['color'] = (0, 0, 0, 255)
		self.font_item_selected['font_name'] = 'Orbitron'
		#self.font_item_selected['font_size'] = 32
		self.font_item_selected['color'] = (50, 50, 50, 255)
		# Alter margin
		self.menu_vmargin = 100
		# Align vertically at the bottom of the screen.
		self.menu_valign = 'bottom'
		# Create the menu items
		items = []
		items.append(MenuItem('Play', self.on_play))
		items.append(MenuItem('Options', self.on_options))
		items.append(MenuItem('Quit', self.on_quit))

		# Finalize the menu
		self.create_menu(items, layout_strategy=paddedVerticalLayout(10))
	
	def on_play(self):
		# Launch game scene.
		import getgame
		director.push(getgame.get_scene())
	
	def on_options(self):
		pass
	
	def on_quit(self):
		# Pop this scene off of the scene stack.
		# This should end the program because there should be no other scenes under the main menu in the stack.
		director.pop()
