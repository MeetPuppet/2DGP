from pico2d import *
import random

class grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class c_Ball:
    def __init__(self):
        self.x, self.y = random.randint(50,750), 580
        self.moveSpeed = random.randint(5,10)
        self.isBig = random.randint(0,1)
        if self.isBig == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

    def update(self):
        if self.isBig == 0:
            if  self.y - 10 > 90 :
                self.y = self.y - self.moveSpeed
            else:
                self.y = 90 + 10

        if self.isBig == 1:
            if self.y - 20 > 90:
                self.y = self.y - self.moveSpeed
            else:
                self.y = 90 + 20

    def render(self):
        self.image.draw(self.x, self.y)

class c_boy:
    def __init__(self):
        self.x, self.y = (random.randint(50,750), 90)
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')


    def update(self):
        self.frame = (self.frame+1)%8
        self.x += 5

    def render(self):
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

balls = [c_Ball() for i in range(20)]

while True:
    handle_events()
    for ball in balls:
        ball.update()
    clear_canvas()

    for ball in balls:
        ball.render()

    update_canvas()
    delay(0.05)

close_canvas()