import cocos
from model.mainmenu import MainMenuModel
from view.mainmenu import MainMenuView
from controller.mainmenu import MainMenuController

def get_scene():
	# Create scene
	scene = cocos.scene.Scene()

	# Setup the model
	model = MainMenuModel()

	# Setup the layers
	view = MainMenuView(model)
	controller = MainMenuController(model)

	# Compile scene
	scene.add(view)
	scene.add(controller)

	return scene
