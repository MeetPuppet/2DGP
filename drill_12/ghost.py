from pico2d import *

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

import game_world

class ghost:
    def __init__(self,point,isRight):
        self.x, self.y = point[0], point[1]
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')
        self.dir = 0
        if isRight == 1:
            self.angle = 3.14 / 2
        else:
            self.angle = -3.14 / 2
        self.frame = 0
        self.event_que = []
        pass
    def update(self):
        pass
    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, 3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 200, 100, 100, -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)

        pass
    pass