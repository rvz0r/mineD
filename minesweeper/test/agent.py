import random
import sys
import pygame as pg


class Agent:
    def __init__(self):
        pass
    playerPos = [0, 0]
    AGENT = pg.image.load("resources/agent.png")

    def show_agent(self, tilesize, SURFACE):
        SURFACE.blit(self.AGENT, (self.playerPos[0] * tilesize, self.playerPos[1] * tilesize))

    def agent_move(self, tilemap, MAPWIDTH, MAPHEIGHT):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        way = random.randint(1, 4)
        print("tilemap:" + str(tilemap[self.playerPos[0]][self.playerPos[1]]) + " " + str(self.playerPos[0]) + " " + str(self.playerPos[1]))
