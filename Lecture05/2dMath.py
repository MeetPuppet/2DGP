import turtle
import random


def move_begier_line(p1,p2,p3):
    t=0.0
    while t <= 1:
        a = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        b = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        turtle.goto(a,b)
        t+=0.01


#for x in range(0,10):

arrow = 0
size = 3
#point = [(random.randint(-300,300),random.randint(-300,300)) for n in range(size)]
#point =[(100,100),(0,150),(-100,100),(-150,0),(-100,-100),(0,-150),(100,-100),(150,0)]
point =[(0,150),(-100,-100),(100,-100)]
turtle.penup()
turtle.goto((-350, -100))
turtle.pendown()
move_begier_line((-350, -100), (-50, 200), (150, -100))
turtle.penup()
turtle.goto((-50, 200))
turtle.pendown()
move_begier_line((-50, 200), (150, -100), (350, 300))
a=1
while True:
    a=1
    #p1 = point[arrow%size]
    #arrow+=1
    #p2 = point[arrow%size]
    #arrow+=1
    #p3= point[arrow%size]
    #move_begier_line(p1,p2,p3)
