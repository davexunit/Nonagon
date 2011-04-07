import cocos
from cocos.scenes.transitions import *
from model.gameover import GameOverModel
from view.gameover import GameOverView
from controller.gameover import GameOverController

def get_scene():
	scene = cocos.scene.Scene()

	model = GameOverModel()
	view = GameOverView(model)
	controller = GameOverController(model)

	scene.add(view)
	scene.add(controller)

	return FadeTransition(scene)
