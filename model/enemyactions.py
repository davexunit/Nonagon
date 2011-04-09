import pyglet
import cocos
from cocos.actions import *
import game
import level

w, h = cocos.director.director.get_window_size()
x_grid_size = 16
y_grid_size = 12
x_unit = w/x_grid_size
y_unit = h/y_grid_size

def MoveToUnit(x, y, duration=4):
    return MoveTo((x*x_unit, y*y_unit), duration)

def square(enemy, border, clockwise=True):
    if clockwise:
        action = Repeat(MoveToUnit(x_grid_size-border, y_grid_size-border) +
                        MoveToUnit(x_grid_size-border, border) +
                        MoveToUnit(border, border) +
                        MoveToUnit(border, y_grid_size-border))
    else:
        action = Repeat(MoveToUnit(border, y_grid_size-border) +
                        MoveToUnit(border, border) +
                        MoveToUnit(x_grid_size-border, border) +
                        MoveToUnit(x_grid_size-border, y_grid_size-border))
    return action

def big_cw_square(enemy):
    return square(enemy, 1, True)

def med_cw_square(enemy):
    return square(enemy, 3, True)

def small_cw_square(enemy):
    return square(enemy, 5, True)

def big_ccw_square(enemy):
    return square(enemy, 1, False)

def med_ccw_square(enemy):
    return square(enemy, 3, False)

def small_ccw_square(enemy):
    return square(enemy, 5, False)

def topleft_to_bottomright(enemy):
    return Repeat(MoveToUnit(1, y_grid_size-1) +
                  MoveToUnit(x_grid_size-1, 1))

def topright_to_bottomleft(enemy):
    return Repeat(MoveToUnit(x_grid_size-1, y_grid_size-1) +
                  MoveToUnit(1,1))

def vertical_dance(enemy):
    return Repeat(MoveToUnit(enemy.x/x_unit, 1) +
                  MoveToUnit(enemy.x/x_unit, y_grid_size-1))

def horizontal_dance(enemy):
    return Repeat(MoveToUnit(1, enemy.y/y_unit) +
                  MoveToUnit(x_grid_size-1, enemy.y/y_unit))
