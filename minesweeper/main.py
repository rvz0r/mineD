import random

import pygame as pg

from minesweeper.agent import Agent
from minesweeper.grid import Grid
from minesweeper.implementation import *



# initializing PyGame module
pg.init()
print('This is our intelligent sprite running through a minefield!')
pg.display.set_caption('Minesweeper')

# player object
agent = Agent()

#grid object
grid = Grid()
grid.legend()

def main():
    grid.set_tilemap()
    grid.generate_tilemap()

    # game loop
    while True & grid.bombcounter != 0:
        #2 linie poniżej są w komentarzu bo w gridzie jest clock w metoda legenda



        grid.display_tilemap()
        # print(timer)

        # Player event

        lol = agent.agent_move(grid.tilemap, grid.bombcounter)

        for x in range(len(lol)):
            agent.playerPos = lol[x]
            agent.show_agent(grid.TILESIZE, grid.SURFACE)
        pg.display.update()
        # player display
        pg.time.wait(1000)



if __name__ == "__main__":
    main()