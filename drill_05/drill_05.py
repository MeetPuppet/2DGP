from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_to_there_01():
    x, y=712, 349
    frameX=0
    frameY=0
    while x>203 or y<535:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frameX * 100, frameY * 100, 100, 100, x, y)
        update_canvas()
        frameX = (frameX + 1) % 8
        if x > 203+1:
            x-=10
            frameX=0
        else:
            x+=1
            frameX=1

        if y < 535+1:
            y+=10
        else:
            y-=1




def move_to_there_02():
    pass


def move_to_there_03():
    pass


def move_to_there_04():
    pass


def move_to_there_05():
    pass


def move_to_there_06():
    pass


def move_to_there_07():
    pass


def move_to_there_08():
    pass


def move_to_there_09():
    pass


def move_to_there_10():
    pass

while True :
    move_to_there_01()
    pass