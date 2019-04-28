import random

import pygame as pg

from minesweeper.agent import Player
from minesweeper.grid import Grid

# initializing PyGame module
pg.init()
print('This is our intelligent sprite running through a minefield!')

# player object

player = Player()
#grid object
grid = Grid()


def main():
    # game loop
    while True:
        #2 linie poniżej są w komentarzu bo w gridzie jest clock w funkcji legenda

        # clock.tick(120)
        # timer = pg.time.get_ticks()


        # print(timer)


        # Player event
        player.agent_move(grid.tilemap, grid.MAPWIDTH, grid.MAPHEIGHT)
        # player display
        player.show_agent(grid.TILESIZE, grid.SURFACE)
        pg.display.update()


if __name__ == "__main__":
    main()
