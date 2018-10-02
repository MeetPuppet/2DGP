from pico2d import *
import random

open_canvas()

back = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

def move_from_to(p1,p2):
    start = p1
    end = p2
    global frame
    t = 0

    while t >= 1:
        clear_canvas()
        back.draw(400,300)
        character.clip_draw(frame[0]*100,frame[1]*100,100,100,start[0]*(1-t)+end[0]*t)
        update_canvas()
        frame[0] = (frame[0]+1)%8
        if end[0]<start[0]:
            frame[1]=1
        else:
            frame[1]=0

while True:

    pass