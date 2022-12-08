from turtle import *
black = 'black'
red = 'red'
blue = 'blue'


t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()

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
    t1.showturtle()
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
    t2.showturtle()
    t2.pendown()
    t2.goto(x+50, y-50)
    t2.penup()
    t2.goto(x+50, y+50)
    t2.pendown()
    t2.goto(x-50, y-50)
    t2.hideturtle()


def circle(x=0, y=0):
    t3.penup()
    t3.goto(x, y-50)
    t3.showturtle()
    t3.pendown()
    t3.circle(50)
    t3.hideturtle()


def check_winner(tiles, tile_coor, game):
    winner = 0
    if tiles[0] == tiles[1] == tiles[2]:
        winner = tiles[0]
        if winner > 0:
            cross(tile_coor[0], tile_coor[2])
    elif tiles[3] == tiles[4] == tiles[5]:
        winner = tiles[3]
        if winner > 0:
            cross(tile_coor[3], tile_coor[5])
    elif tiles[6] == tiles[7] == tiles[8]:
        winner = tiles[6]
        if winner > 0:
            cross(tile_coor[6], tile_coor[8])
    elif tiles[0] == tiles[3] == tiles[6]:
        winner = tiles[0]
        if winner > 0:
            cross(tile_coor[0], tile_coor[6])
    elif tiles[1] == tiles[4] == tiles[7]:
        winner = tiles[1]
        if winner > 0:
            cross(tile_coor[1], tile_coor[7])
    elif tiles[2] == tiles[5] == tiles[8]:
        winner = tiles[2]
        if winner > 0:
            cross(tile_coor[2], tile_coor[8])
    elif tiles[0] == tiles[4] == tiles[8]:
        winner = tiles[0]
        if winner > 0:
            cross(tile_coor[0], tile_coor[8])
    elif tiles[2] == tiles[4] == tiles[6]:
        winner = tiles[2]
        if winner > 0:
            cross(tile_coor[2], tile_coor[6])
    if winner == 1:
        print("Cross win")
        dance(t2)
    if winner == 2:
        print("Zero win")
        dance(t3)

    game = False


def cross(start, finish):
    t1.width(7)
    t1.penup()
    t1.goto(*start)
    t1.pendown()
    t1.goto(*finish)
    t1.penup()


def dance(t):
    t.speed(50)
    for i in range(10):
        t.penup()
        t.goto(-250, 250)
        t.pendown()
        for j in range(25):
            t.forward(10)
            t.left(10)
