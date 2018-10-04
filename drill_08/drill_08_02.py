from pico2d import *
import random

def draw_p4_line(prev,start,end,next):
    t=0
    while t<=1:
        x=((-t**3+2*t**2-t)*prev[0]+(3*t**3-5*t**2+2)*start[0]+(-3*t**3+4*t**2+t)*end[0]+(t**3-t**2)*next[0])*0.5
        y=((-t**3+2*t**2-t)*prev[1]+(3*t**3-5*t**2+2)*start[1]+(-3*t**3+4*t**2+t)*end[1]+(t**3-t**2)*next[1])*0.5
        t+=0.01





arrow=0
size=10
points=[(random.randint(0+1,800-1),random.randint(0+1,600-1)) for i in range(size)]

while True:
    p1=points[arrow%size]
    arrow+=1
    p2=points[arrow%size]
    arrow+=1
    p3=points[arrow%size]
    arrow+=1
    p4=points[arrow%size]
    draw_p4_line(p1,p2,p3,p4)
    arrow-=2