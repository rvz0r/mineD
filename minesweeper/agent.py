import random
import sys
from minesweeper.pathfinding import GraphPath
from minesweeper.grid import Grid

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
        math_grid = GraphPath(15, 15)
        math_grid.filler(Grid().tilemap)
        start, goal = (0, 0), (14, 14)
        mines = math_grid.math(math_grid, start, goal)
        bool = 1
        while True:
            if bool == 1:
                goal = list(mines.keys())[list(mines.values()).index(min(mines.values()))]
                Path = math_grid.path(goal)
                pg.time.wait(750)
                self.playerPos[0] = Path[0][0]
                self.playerPos[1] = Path[0][1]
                del Path[0]
                if Path == []:
                    bool == 0
            if bool == 0:
                start = (self.playerPos[0],self.playerPos[1])
                goal = list(mines.keys())[list(mines.values()).index(max(mines.values()))]
                mines = math_grid.math(math_grid, start, goal)


