from turtle import *
from random import shuffle, randint
from time import sleep
from settings import field, cros, circle


field()

tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0]

print("Cross turn")
turn = int(input("Enter tile number"))
if tiles[turn-1] == 0:
    cros(-100, 100)
    tiles[turn-1] = 1
    print(tiles)


print("Circle turn")
turn = int(input("Enter tile number"))
if tiles[turn-1] == 0:
    circle(100, 100)
    tiles[turn-1] = 2
    print(tiles)


#cros(-100, 100)
#circle(100, 100)
exitonclick()
