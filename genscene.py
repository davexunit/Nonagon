"""This script will create the necessary source files for a new scene.
For each scene 4 python source files have to be created so there is a lot of boilerplate.
This script does it all for you. Isn't that nice? :]
Usage: python genscene.py Game
"""
import sys
import os

def check(filename):
	if os.path.exists(filename):
		print "File %s already exists. Aborting." % filename
		exit()

if sys.argv < 2:
	print "Usage: %s [scene_name]" % sys.argv[0]
	exit()

# Scene name
scene_name = sys.argv[1]
# Convert argument to lowercase for naming the source files
module_name = scene_name.lower()

# Create model file
model_filename = 'model/%s.py' % module_name
print 'Creating %s' % model_filename
check(model_filename)
model = open(model_filename, 'w')
model.write('import pyglet\n\n\
class %sModel(pyglet.event.EventDispatcher):\n\
	def __init__(self):\n\
		super(%sModel, self).__init__()\n' % (scene_name, scene_name))
model.close()

# Create view file
view_filename = 'view/%s.py' % module_name
print 'Creating %s' % view_filename
check(view_filename)
view = open(view_filename, 'w')
view.write('import cocos\n\n\
class %sView(cocos.layer.Layer):\n\
	def __init__(self, model):\n\
		super(%sView, self).__init__()\n\
		self.model = model\n' % (scene_name, scene_name))
view.close()

# Create controller file
controller_filename = 'controller/%s.py' % module_name
print 'Creating %s' % controller_filename
check(controller_filename)
controller = open(controller_filename, 'w')
controller.write('import cocos\n\n\
class %sController(cocos.layer.Layer):\n\
	is_event_handler = True\n\n\
	def __init__(self, model):\n\
		super(%sController, self).__init__()\n\
		self.model = model\n' % (scene_name, scene_name))
view.close()

# Create root level file
root_filename = 'get%s.py' % module_name
print 'Creating %s' % root_filename
check(root_filename)
root = open(root_filename, 'w')
root.write('import cocos\n\
from model.%s import %sModel\n\
from view.%s import %sView\n\
from controller.%s import %sController\n\n\
def get_scene():\n\
	scene = cocos.scene.Scene()\n\n\
	model = %sModel()\n\
	view = %sView(model)\n\
	controller = %sController(model)\n\n\
	scene.add(view)\n\
	scene.add(controller)\n\n\
	return scene\n' % (module_name, scene_name, module_name, scene_name, module_name, scene_name, scene_name, scene_name, scene_name))
root.close()

