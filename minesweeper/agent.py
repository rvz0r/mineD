
import sys

import pygame as pg

from minesweeper.test import goal
from minesweeper.test import agentmove

class Agent:

    playerPos = [0, 0]
    AGENT = pg.image.load("resources/agent.png")
    length = 0
    previous_goal = (0, 0)
    goal = None
    count1 = 0
    def __init__(self):
        pass

    def show_agent(self, tilesize, SURFACE):
        SURFACE.blit(self.AGENT, (self.playerPos[0] * tilesize, self.playerPos[1] * tilesize))

    def agent_move(self, tilemap, bombcounter):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        if self.count1 == 0:
            self.count1 = 1
            self.goal = goal(tilemap, bombcounter)
        else:
            self.previous_goal = self.goal
            self.goal = goal(tilemap, bombcounter)
        return agentmove(self.previous_goal, self.goal)




