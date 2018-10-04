from pico2d import *
import random

def draw_p4_line(prev,start,end,next):
    global frame
    global character
    t=0
    clear_canvas()
    while t<=1:
        x=((-t**3+2*t**2-t)*prev[0]+(3*t**3-5*t**2+2)*start[0]+(-3*t**3+4*t**2+t)*end[0]+(t**3-t**2)*next[0])*0.5
        y=((-t**3+2*t**2-t)*prev[1]+(3*t**3-5*t**2+2)*start[1]+(-3*t**3+4*t**2+t)*end[1]+(t**3-t**2)*next[1])*0.5
        back.draw(400,300)
        character.clip_draw(frame[0]*100,frame[1]*100,100,100,x,y)
        update_canvas()
        frame[0]=(frame[0]+1)%8
        if(start>end):
            frame[1]=0
        else:
            frame[1]=1
        t+=0.01
        delay(0.001)



open_canvas()
back = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')



frame=[0,0]
arrow=0
size=10
points=[(random.randint(100+1,700-1),random.randint(100+1,500-1)) for i in range(size)]

while True:
    p1=points[arrow%size]
    arrow+=1
    p2=points[arrow%size]
    arrow+=1
    p3=points[arrow%size]
    arrow+=1
    p4=points[arrow%size]
    draw_p4_line(p1,p2,p3,p4)
    character.(frame[0]*100,frame[1]*100,100,100,p3[0],p3[1])
    arrow-=2

close_canvas()