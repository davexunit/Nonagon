import cocos
import game
from cocos.path import Bezier

class Wave(cocos.cocosnode.CocosNode):
    def __init__(self, enemy_list):
        super(Wave, self).__init__()
        w,h = cocos.director.director.get_window_size()
        for i, enemy_tuple in enumerate(enemy_list):
            vertex_count, enemy_action = enemy_tuple
            if enemy_action == None:
                # Construct default action
                pass
            enemy = game.EnemyPolygon(vertex_count)
            enemy.position =  w/len(enemy_list)*(i+0.5), h-100
            self.add(enemy)
                

"""
class Level(cocos.cocosnode.CocosNode):


    def __init__(self):
        
        
        


        def create_enemy_path(self, x_dest, y_dest, bend):
            rel_start = (0,0)
            rel_end = (x_dest-self.ship.x, y_dest-self.ship.y)

            rel_start_handle = rel_start
            rel_end_handle = rel_end

            if y_dest < self.ship.y:
                bend = (bend * 2) % 3

                if bend == self.BEND_UP:
                    rel_start_handle = (rel_start[0], rel_start[1] + rel_end[1])
                    rel_end_handle = (rel_end[0] - rel_start[0], rel_end[1])
                elif bend == self.BEND_DOWN:
                    rel_start_handle = (rel_start[0] + rel_end[0], rel_start[1])
                    rel_end_handle = (rel_end[0] , rel_end[1] - rel_start[0])

                self.dot_sprites[0].position = self.ship.position
                self.dot_sprites[1].position = (x_dest, y_dest)
                path = Bezier(rel_start, rel_end, rel_start_handle, rel_end_handle)
                return path
"""
