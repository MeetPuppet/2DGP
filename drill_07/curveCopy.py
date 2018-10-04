import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(800, 600)
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
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())




def draw_curve_3_points(p1, p2, p3):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    t=0.0
    while t<=1+0.01:
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        t+=0.01
        draw_point((x,y))



def draw_curve_4_points(prev, start, end, next):
    draw_big_point(start)
    draw_big_point(end)

    for i in range(0,100,5):
        t = i/100
        x = ((-t**3+2*t**2-t)*prev[0]+(3*t**3-5*t**2+2)*start[0]+(-3*t**3+4*t**2+t)*end[0]+(t**3-t**2)*next[0])*0.5
        y = ((-t**3+2*t**2-t)*prev[1]+(3*t**3-5*t**2+2)*start[1]+(-3*t**3+4*t**2+t)*end[1]+(t**3-t**2)*next[1])*0.5
        draw_point((x,y))

prepare_turtle_canvas()

point = [(-30, 20), (40, 35), (30, -30), (-20, -20)]
#point = [(random.randint(-300,300),random.randint(-250,250)) for i in range(10)]
arrow=0
size=len(point)
print(size)
while True:
    p1=point[arrow%size]
    arrow+=1
    p2=point[arrow%size]
    arrow+=1
    p3=point[arrow%size]
    arrow+=1
    p4=point[arrow%size]
    draw_curve_4_points(p1,p2,p3,p4)
    arrow-=2




turtle.done()