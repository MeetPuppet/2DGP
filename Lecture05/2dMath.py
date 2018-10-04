import turtle
import random


def move_begier_line(p1,p2,p3):
    global t
    while t <= 1+0.01:
        print(t)
        a = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        b = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        turtle.goto(a,b)
        t+=0.01

def move_begier_mixed_line(p1,p2,p3,p4):
    t=0.0
    while t <= 1+0.01:
        a = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])*0.5
        b = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])*0.5

        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2

        turtle.goto(a,b)
        t+=0.01


#for x in range(0,10):

arrow = 0
size = 4
#point = [(random.randint(-300,300),random.randint(-300,300)) for n in range(size)]
#point =[(100,100),(0,150),(-100,100),(-150,0),(-100,-100),(0,-150),(100,-100),(150,0)]
point = [(-300, 200), (400, 350), (300, -300), (-200, -200)]
t=0
"""
turtle.penup()
turtle.goto((-350, -100))
turtle.pendown()
move_begier_line((-350, -100), (-50, 200), (150, -100),0,1)

turtle.penup()
turtle.goto((150, -100))
turtle.pendown()
move_begier_line((-50, 200), (150, -100), (350, 300),0.0,1)

turtle.penup()
turtle.goto((-350, -100))
turtle.pendown()
move_begier_line((-350, -100), (-50, 200), (150, -100),0,0.5)

move_begier_mixed_line((-350, -100), (-50, 200), (150, -100),(350,300))

turtle.penup()
turtle.goto((150, -100))
turtle.pendown()
move_begier_line((-50, 200), (150, -100), (350, 300),0.5,1)
a=1
"""
while True:
    t=0
    p1 = point[arrow%size]
    arrow+=1
    p2 = point[arrow%size]
    arrow+=1
    p3= point[arrow%size]
    move_begier_line(p1,p2,p3)
