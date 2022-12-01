from turtle import *
black = 'black'
red = 'red'
blue = 'blue'


t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.color(black)
t1.width(5)
t1.speed(5)

t2.color(blue)
t2.width(5)
t2.speed(5)
t2.shape('triangle')

t3.color(red)
t3.width(5)
t3.speed(5)
t3.shape('circle')


def field(x=-150, y=150):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    i = 0
    while i < 4:
        t1.forward(300)
        t1.right(90)
        i += 1    # i = i + 1
    t1.forward(100)
    t1.right(90)
    t1.forward(300)
    t1.left(90)
    t1.forward(100)
    t1.left(90)
    t1.forward(300)
    t1.right(90)
    t1.forward(100)
    t1.right(90)
    t1.forward(100)
    t1.right(90)
    t1.forward(300)
    t1.left(90)
    t1.forward(100)
    t1.left(90)
    t1.forward(300)
    t1.hideturtle()


def cros(x=0, y=0):
    t2.penup()
    t2.goto(x-50, y+50)
    t2.pendown()
    t2.goto(x+50, y-50)
    t2.penup()
    t2.goto(x+50, y+50)
    t2.pendown()
    t2.goto(x-50, y-50)


def circle(x=0, y=0):
    t3.penup()
    t3.goto(x, y-50)
    t3.pendown()
    t3.circle(50)
