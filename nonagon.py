"""This is the entry point to the game. It initializes cocos2d, creates the game window and launches the initial game scene.
"""
import cocos
from cocos.director import director
import pyglet
import getmainmenu

# Tell pyglet where our game resources are located
pyglet.resource.path.append('media/images')
pyglet.resource.path.append('media/sounds')
pyglet.resource.reindex()
pyglet.font.add_directory('media/fonts')

# Initialize game window
director.init(width=800, height=600)
director.show_FPS = True

# Simply start up the game with our main menu scene.
# If we get far enough we should have a fancy intro scene that comes before the main menu.
director.run(getmainmenu.get_scene())
