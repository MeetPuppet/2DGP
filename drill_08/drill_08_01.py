import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8,0.9,0)
    turtle.dot(15)
    turtle.write('     '+str(p))

def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())

def draw_p4_line(prev,start,end,next):
    t=0
    while t<=1+0.01:
        x=()*0.5
        t+=0.01
    pass

points=[(-300,200),(400,350),(300,-300),(-200,-200)]

arrow=0
size=len(points)

while True:
    pass