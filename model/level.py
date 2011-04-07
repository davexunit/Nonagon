import cocos
import game
from cocos.path import Bezier

class Wave(cocos.cocosnode.CocosNode):
    def __init__(self, enemy_list):
        super(Wave, self).__init__()
        w,h = cocos.director.director.get_window_size()
        for i, enemy_tuple in enumerate(enemy_list):
            vertex_count, enemy_action = enemy_tuple
            enemy = game.EnemyPolygon(vertex_count)
            enemy.position =  w/len(enemy_list)*(i+0.5), h-100
            self.add(enemy)
            if enemy_action != None:
                enemy.do(enemy_action)
            else:
                path = create_enemy_path(enemy, 400, 300, BEND_UP)
                action = cocos.actions.Bezier(path, 5)
                enemy.do(action)

                
BEND_NONE = 0
BEND_DOWN = 1
BEND_UP = 2
def create_enemy_path(enemy, x_dest, y_dest, bend):
            rel_start = (0,0)
            rel_end = (x_dest-enemy.x, y_dest-enemy.y)

            rel_start_handle = rel_start
            rel_end_handle = rel_end

            if y_dest < enemy.y:
                bend = (bend * 2) % 3

                if bend == BEND_UP:
                    rel_start_handle = (rel_start[0], rel_start[1] + rel_end[1])
                    rel_end_handle = (rel_end[0] - rel_start[0], rel_end[1])
                elif bend == BEND_DOWN:
                    rel_start_handle = (rel_start[0] + rel_end[0], rel_start[1])
                    rel_end_handle = (rel_end[0] , rel_end[1] - rel_start[0])

#                self.dot_sprites[0].position = enemy.position
#                self.dot_sprites[1].position = (x_dest, y_dest)
                path = Bezier(rel_start, rel_end, rel_start_handle, rel_end_handle)
                return path

