import cocos
from model.game import GameModel
from view.game import GameView
from controller.game import GameController

def get_scene():
	scene = cocos.scene.Scene()

	model = GameModel()
	view = GameView(model)
	controller = GameController(model)

	model.next_level()

	scene.add(view)
	scene.add(controller)

	return scene
