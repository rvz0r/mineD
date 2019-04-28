import random
import sys

import pygame as pg


class Player:


    def __init__(self):
        pass

    def move_right(self):
        x += 1

    def move_left(self):
        x -= 1

    def move_up(self):
        y += 1

    def move_down(self):
        y -= 1

    def show_agent(self, tilesize, SURFACE, PLAYER, playerPos):
        SURFACE.blit(PLAYER, (playerPos[0] * tilesize, playerPos[1] * tilesize))

    def player_pos(self):
        print(x + " " + y)

    def agent_move(self, tilemap, playerPos, MAPWIDTH, MAPHEIGHT):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        while True:
            way = random.randint(1, 4)
            # print(way)
            pg.time.wait(200)
            print("tilemap:" + str(tilemap[playerPos[0]][playerPos[1]]))

            if way == 1 and playerPos[0] < MAPWIDTH - 1:
                if playerPos[0] < 15:
                    if tilemap[playerPos[0] + 1][playerPos[1]] != 2:
                        playerPos[0] += 1
                        print(playerPos[0], playerPos[1])
                        break
            if way == 2 and playerPos[0] > 0:
                if playerPos[0] < 15:
                    if tilemap[playerPos[0] - 1][playerPos[1]] != 2:
                        playerPos[0] -= 1
                        print(playerPos[0], playerPos[1])
                        break
            if way == 3 and playerPos[1] < MAPHEIGHT - 1:
                if playerPos[0] < 15:
                    if tilemap[playerPos[0]][playerPos[1] + 1] != 2:
                        playerPos[1] += 1
                        print(playerPos[0], playerPos[1])
                break
            if way == 4 and playerPos[1] > 0:
                if playerPos[0] < 15:
                    if tilemap[playerPos[0]][playerPos[1] - 1] != 2:
                        playerPos[1] -= 1
                        print(playerPos[0], playerPos[1])
                        break

'''
            if way == 1 and playerPos[0] < MAPWIDTH - 1 and 
                playerPos[0] += 1
                print(playerPos[0], playerPos[1])
                break
            if way == 2 and playerPos[0] > 0 and tilemap[playerPos[0] - 1][playerPos[1]] != 2:
                playerPos[0] -= 1
                print(playerPos[0], playerPos[1])
                break
            if way == 3 and playerPos[1] < MAPHEIGHT - 1 and tilemap[playerPos[0]][playerPos[1] + 1] != 2:
                playerPos[1] += 1
                print(playerPos[0], playerPos[1])
                break
            if way == 4 and playerPos[1] > 0 and tilemap[playerPos[0]][playerPos[1] - 1] != 2:
                playerPos[1] -= 1
                print(playerPos[0], playerPos[1])
                break
'''
