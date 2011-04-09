import pyglet
from pyglet.window import key
import cocos
from cocos.menu import *
from cocos.director import director
from collections import deque

class MainMenuModel(pyglet.event.EventDispatcher):
	"""Holds state for the Main Menu scene.
	"""
	def __init__(self):
		super(MainMenuModel, self).__init__()
		self.player = pyglet.media.Player()
		self.player.eos_action = pyglet.media.Player.EOS_LOOP
		self.music = pyglet.resource.media('Intro.mp3')
		self.player.queue(self.music)
		self.multiplex = cocos.layer.MultiplexLayer(MainMenu(self), Instructions(self))

class Instructions(cocos.layer.Layer):
	"""A nice little layer for displaying instructions for the player.
	"""
	is_event_handler = True

	def __init__(self, model):
		super(Instructions, self).__init__()
		self.model = model
		# Queue for our instruction messages
		self.messages = deque()
		self.messages.append('Press ENTER to move to the next instruction')
		self.messages.append('This game is a shoot-em-up with a math puzzle twist.\nYou are Sigma, the ultimate Mathemagician.\nYour enemies are an angry group of regular polygons.')
		self.messages.append('They have shields to protect themselves, but they have a weakness...\n...They have a "kill vertex" that is marked by a large dot.')
		self.messages.append('You must shoot the kill vertex to kill the enemy.\nTo do that you must fire transformation bullets to make the kill vertex face downward.')
		self.messages.append('If you manage to kill all of the minions, you will fight the mighty Nonagon!')
		self.messages.append('Control your ship with the UP, DOWN, LEFT, and RIGHT arrow keys')
		self.messages.append('Press A to fire a ROTATE CLOCKWISE bullet')
		self.messages.append('Press S to fire a ROTATE COUNTER-CLOCKWISE bullet')
		self.messages.append('Press D to fire a FLIP LEFT bullet')
		self.messages.append('Press F to fire a FLIP RIGHT bullet')
		self.messages.append('Press SPACE to fire a DAMAGE bullet')
		self.messages.append('Do NOT hit an enemy with same transformation bullet twice in a row!\nThey will be annoyed by this and become un-transformable for a short period of time.')
		self.messages.append('If you kill 9 enemies without dying or hitting one with the same transformation bullet twice in a row, you will gain an extra life!\nTrust me, you\'ll need it.')
		self.messages.append('GOOD LUCK!')
		# Create text box
		pad = 10
		w, h = director.get_window_size()
		self.text = cocos.text.Label('', multiline=True, width=w-pad*2, color=(0, 0, 0, 255), font_name='Orbitron', font_size=32, anchor_x='center', anchor_y='center')
		self.text.position = w/2, 200
		self.next_message()
		# Add text box to node
		self.add(self.text)
		
	def next_message(self):
		if len(self.messages) == 0:
			self.model.multiplex.switch_to(0)
			return 
		self.text.element.text = self.messages.popleft()
	
	def on_key_press(self, symbol, modifiers):
		if symbol == key.ENTER:
			self.next_message()

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
	"""
	def __init__(self, model):
		super(MainMenu, self).__init__('')
		self.model = model
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
		items.append(MenuItem('Instructions', self.on_instructions))
		items.append(MenuItem('Quit', self.on_quit))

		# Finalize the menu
		self.create_menu(items, layout_strategy=paddedVerticalLayout(10))
	
	def on_play(self):
		# Launch game scene.
		import getgame
		director.push(getgame.get_scene())
	
	def on_instructions(self):
		# Switch to the instructions layer
		self.model.multiplex.switch_to(1)
	
	def on_quit(self):
		# Pop this scene off of the scene stack.
		# This should end the program because there should be no other scenes under the main menu in the stack.
		director.pop()
