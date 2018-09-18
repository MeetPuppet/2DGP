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
        if x > 203:
            x-=1
            frameY=0
        elif x < 203:
            x+=1
            frameY=1

        if y < 535:
            y+=1
        elif y > 535:
            y-=1

def move_to_there_02():
    x, y=203, 535
    frameX=0
    frameY=0
    while x>132 or y>243:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frameX * 100, frameY * 100, 100, 100, x, y)
        update_canvas()
        frameX = (frameX + 1) % 8
        if x > 132:
            x-=1
            frameY=0
        elif x<132:
            x+=1
            frameY=1

        if y < 243:
            y+=1
        elif y>243:
            y-=1


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

def move_arround():
    move_to_there_01()
    move_to_there_02()


while True :
    move_arround()
    pass