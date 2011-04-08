import cocos
from cocos.scenes.transitions import *
from model.victory import VictoryModel
from view.victory import VictoryView
from controller.victory import VictoryController

def get_scene(score):
	scene = cocos.scene.Scene()

	model = VictoryModel(score)
	view = VictoryView(model)
	controller = VictoryController(model)

	scene.add(view)
	scene.add(controller)

	return FadeTransition(scene)
