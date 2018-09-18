from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

#코드의 의도가 확실해짐
def move_from_center_to_right():
    x,y = 800//2,90
    while x<800 - 25:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x+=10
        delay(0.01)
    #완성 후  pass는 제거

def move_up():
    x,y=800-25,90
    while y<600-50:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y+=10
        delay(0.01)

def move_left():
    x,y=800-25,600-50
    while x>0+25:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x-=10
        delay(0.01)

def move_down():
    x,y = 0+25,600-50
    while y>0+90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y-=10
        delay(0.01)

def move_left_to_center():
    x,y = 0+25,0+90
    while x<800//2:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x+=10
        delay(0.01)

def make_rectangle():
    move_from_center_to_right()#첫 코드가 함수?
    move_up()
    move_left()
    move_down()
    move_left_to_center()

import math
#각도바꾸는 계산식이 있다고한다. 함 보자
def make_circle():
    cx, cy, r = 800//2,600//2,(600-180)//2
    degree = -90
    while degree <270:
        radian=math.radians(degree)
        x = cx+r*math.cos(radian)
        y = cy+r*math.sin(radian)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        degree+=1
        delay(0.01)

while True:
    make_rectangle()
    make_circle()



close_canvas()

"""
함수의 이름에서 앞 단어는 동사여야한다.
ex. rectangle -> make_rectangle

"""