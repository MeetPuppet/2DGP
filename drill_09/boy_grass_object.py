from pico2d import *
import random

# Game object class here
class c_Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class c_boy:
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame+1)%8
        self.x+=5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

# initialization code
team = [c_boy(i*10,90) for i in range(11)]

while True:
    handle_events()
# game main loop code
    for boy in team:
        boy.update()
    clear_canvas()

# finalization code
    for boy in team:
        boy.draw()

    update_canvas()
    delay(0.05)