from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def move_to_there(startX,startY,endX,endY):
    x, y=startX, startY
    frameX=0
    frameY=0
    while x!=endX or y!=endY:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frameX * 100, frameY * 100, 100, 100, x, y)
        update_canvas()
        frameX = (frameX + 3) % 8
        if x > endX:
            x-=0.5
            frameY=0
        elif x<endX:
            x+=0.5
            frameY=1

        if y < endY:
            y+=0.5
        elif y>endY:
            y-=0.5

def move_arround():
    move_to_there(712,349,203,530)
    move_to_there(203,535,132,243)
    move_to_there(132,243,535,470)
while True :
    move_arround()
    pass