from pico2d import *
import random

def point_4_begier_line(prev,start,end,next):
    global frame
    t = 0

    while t <= 1:
        clear_canvas()
        back.draw(400, 300)
        x = ((-t**3+2*t**2-t)*prev[0]+(3*t**3-5*t**2+2)*start[0]+(-3*t**3+4*t**2+t)*end[0]+(t**3-t**2)*next[0])*0.5
        y = ((-t**3+2*t**2-t)*prev[1]+(3*t**3-5*t**2+2)*start[1]+(-3*t**3+4*t**2+t)*end[1]+(t**3-t**2)*next[1])*0.5
        character.clip_draw(frame[0] * 100, frame[1] * 100, 100, 100, x, y)
        update_canvas()
        frame[0] = (frame[0] + 1) % 8
        t += 0.1
        if end[0] < start[0]:
            frame[1] = 1
        else:
            frame[1] = 0
        delay(0.05)



open_canvas()
back = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

frame = [0,0]
arrow=0
size = 10
points = [(random.randint(0,800-1),random.randint(0,600-1)) for i in range(size)]

while True:
    p1=points[arrow%size]
    arrow+=1
    p2=points[arrow%size]
    arrow+=1
    p3=points[arrow%size]
    arrow+=1
    p4=points[arrow%size]
    point_4_begier_line(p1,p2,p3,p4)
    arrow-=2


close_canvas()