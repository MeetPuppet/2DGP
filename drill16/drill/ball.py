import random
from pico2d import *
import game_world
import game_framework

import main_state

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(200, 1600), random.randint(200, 1100), 0
        self.dirx, self.diry = 0,0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10


    def set_center_object(self, boy):
        self.center_object = boy

    def draw(self):
        self.image.draw(self.x, self.y )
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x = self.x - self.dirx * game_framework.frame_time
        self.y = self.y - self.diry * game_framework.frame_time
        pass

    def mover(self,point):
        print(point)
        if point[0]<0:
            self.dirx = point[0]
            pass
        elif point[0]>0:
            self.dirx = point[0]
            pass
        else: self.dirx=0

        if point[1] < 0:
            self.diry = point[1]
            pass
        elif point[1] > 0:
            self.diry = point[1]
            pass
        else: self.diry=0
        pass
