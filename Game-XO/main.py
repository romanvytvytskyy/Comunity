from turtle import *
from random import shuffle, randint
from time import sleep
from settings import field, cros, circle, dance, check_winner


field()


tile_coor = [(-100, 100), (0, 100), (100, 100),
             (-100, 0), (0, 0), (100, 0), (-100, -100), (0, -100), (100, -100)]
tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0]


game = True
turn = 1  # 1 - X-turn, 2- 0-turn


while game:  # ==  while game == True:
    if turn == 1:
        print("Cross turn")
        turn_tile = int(input("Enter tile number (1-9)"))
        if 0 < turn_tile < 10 and tiles[turn_tile-1] == 0:
            if turn_tile == 1:
                cros(-100, 100)
            elif turn_tile == 2:
                cros(0, 100)
            elif turn_tile == 3:
                cros(100, 100)
            elif turn_tile == 4:
                cros(-100, 0)
            elif turn_tile == 5:
                cros(0, 0)
            elif turn_tile == 6:
                cros(100, 0)
            elif turn_tile == 7:
                cros(-100, -100)
            elif turn_tile == 8:
                cros(0, -100)
            elif turn_tile == 9:
                cros(100, -100)
            else:
                print("Enter tile number from 1 to 9")
            tiles[turn_tile-1] = 1
            turn = 2
            print(tiles)
        else:
            print("Wrong tile. Or tile is ocupated")
        check_winner(tiles, tile_coor, game)
    if turn == 2:
        print("Circle turn")
        turn_tile = int(input("Enter tile number (1-9)"))
        if 0 < turn_tile < 10 and tiles[turn_tile-1] == 0:
            if turn_tile == 1:
                circle(-100, 100)
            elif turn_tile == 2:
                circle(0, 100)
            elif turn_tile == 3:
                circle(100, 100)
            elif turn_tile == 4:
                circle(-100, 0)
            elif turn_tile == 5:
                circle(0, 0)
            elif turn_tile == 6:
                circle(100, 0)
            elif turn_tile == 7:
                circle(-100, -100)
            elif turn_tile == 8:
                circle(0, -100)
            elif turn_tile == 9:
                circle(100, -100)
            else:
                print("Enter tile number from 1 to 9")
            tiles[turn_tile-1] = 2
            print(tiles)
            turn = 1
        else:
            print("Wrong tile. Or tile is ocupated")
        check_winner(tiles, tile_coor, game)


exitonclick()
