from pico2d import *

import game_framework
import time
import random

# ghost Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# ghost Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

import game_world

class ghost:
    def __init__(self,point,isRight):
        self.x, self.y = point[0], point[1]
        self.frameX, self.frameY = 0, 0
        # ghost is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')

        self.state = 0
        self.pivot = 25
        self.time = 0
        self.dir = 0
        if isRight == 1:
            self.dir = 1
            self.angle = 3.14 / 2
        else:
            self.dir = -1
            self.angle = -3.14 / 2

        self.alphaOn = True
        self.alpha = 0.2
        self.event_que = []
        pass
    def update(self):
        '''
        if self.alphaOn == True:
            self.alpha += (FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) / 50
        else:
            self.alpha -= (FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) / 50

        if self.alpha >= 0.6:
            self.alphaOn = False
        elif self.alpha <= 0.1:
            self.alphaOn = True
'''
        curtime = game_framework.frame_time
        if game_framework.frame_time - int(game_framework.frame_time) < 1:
            self.alpha = (random.randint(1,8))/10

        if self.state == 0:
            self.time = game_framework.frame_time
            if self.dir == 1:
                self.angle -= (game_framework.frame_time) / 2
                self.pivot = (self.time*0)+(self.pivot*(1 - self.time))
            else:
                self.angle += (game_framework.frame_time) / 2
                self.pivot = (self.time*0)+(self.pivot*(1 - self.time))

            if self.dir == 1 and self.angle < 0:
                self.state = 1
            elif self.dir == -1 and self.angle > 0:
                self.state = 1

            pass
        else:
            if self.dir == 1:
                self.angle += game_framework.frame_time*8
                self.x += ((math.cos(self.angle)) * RUN_SPEED_PPS)*game_framework.frame_time*12
                self.y -= (-(math.sin(self.angle)) * RUN_SPEED_PPS)*game_framework.frame_time*12
            elif self.dir == -1:
                self.angle -= game_framework.frame_time*8
                self.x -= ((math.cos(self.angle)) * RUN_SPEED_PPS)*game_framework.frame_time*12
                self.y += (-(math.sin(self.angle)) * RUN_SPEED_PPS)*game_framework.frame_time*12



            pass
        self.image.opacify(self.alpha)
        if self.state != 0:
            self.frameX = (self.frameX + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        pass
    def draw(self):
        if self.state == 0:
            if self.dir == 1:
                self.image.clip_composite_draw(int(self.frameX) * 100, 300, 100, 100, self.angle, '', self.x - self.pivot, self.y - self.pivot, 100, 100)
            else:
                self.image.clip_composite_draw(int(self.frameX) * 100, 200, 100, 100, self.angle, '', self.x + self.pivot, self.y - self.pivot, 100, 100)
        else:
            if self.dir == 1:
                self.image.clip_composite_draw(int(self.frameX) * 100, 100, 100, 100, self.angle, '', self.x - self.pivot, self.y - self.pivot, 100, 100)
            else:
                self.image.clip_composite_draw(int(self.frameX) * 100, 0, 100, 100, self.angle, '', self.x + self.pivot, self.y - self.pivot, 100, 100)


        pass
    pass