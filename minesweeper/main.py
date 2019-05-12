import random

import pygame as pg

from minesweeper.agent import Agent

from minesweeper.pathfinding import GraphPath

from minesweeper.grid import Grid

# initializing PyGame module
pg.init()
print('This is our intelligent sprite running through a minefield!')
pg.display.set_caption('Minesweeper')
# player object
agent = Agent()
#grid object
grid = Grid()
grid.legend()
start=(0, 0)
goal=(14, 14)


def main():
    mines = {}
    grid.set_tilemap()
    grid.generate_tilemap()
    math_grid = GraphPath(15, 15)


    # game loop
    while True:
        #2 linie poniżej są w komentarzu bo w gridzie jest clock w funkcji legenda

        # clock.tick(120)
        # timer = pg.time.get_ticks()
        math_grid.filler(grid.tilemap)
        mines = math_grid.math(math_grid, start, goal)
        grid.display_tilemap()
        # print(timer)


        # Player event
        agent.agent_move(grid.tilemap, grid.MAPWIDTH, grid.MAPHEIGHT)
        # player display
        agent.show_agent(grid.TILESIZE, grid.SURFACE)
        pg.display.update()


if __name__ == "__main__":
    main()
