from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def move_from_to(startX,startY,endX,endY):
    x, y=startX, startY
    frameX=0
    frameY=0
    while x!=endX or y!=endY:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frameX * 100, frameY * 100, 100, 100, x, y)
        update_canvas()
        frameX = (frameX + 1) % 8
        if x > endX:
            x-=1
            frameY=0
        elif x<endX:
            x+=1
            frameY=1

        if y < endY:
            y+=1
        elif y>endY:
            y-=1

def move_arround():
    move_from_to(712,349,203,530)
    move_from_to(203,535,132,243)
    move_from_to(132,243,535,470)
    move_from_to(535,470,477,203)
    move_from_to(477,203,715,136)

    move_from_to(715,136,316,225)
    move_from_to(316,225,510,92)
    move_from_to(510,92,692,518)
    move_from_to(692,518,682,336)
    move_from_to(682,336,712,349)
while True :
    move_arround()
