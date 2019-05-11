import random

import pygame as pg

from minesweeper.agent import Agent
from minesweeper.grid import Grid
from minesweeper.implementation import *
from minesweeper.graph import *
from minesweeper.astarsearch import *
from minesweeper.queue import *

# initializing PyGame module
pg.init()
print('This is our intelligent sprite running through a minefield!')
pg.display.set_caption('Minesweeper')

# player object
agent = Agent()

#grid object
grid = Grid()
grid.legend()

#example graph
example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}

breadth_first_search_1(example_graph, 'A')



def main():
    grid.set_tilemap()
    grid.generate_tilemap()

    # game loop
    while True:
        #2 linie poniżej są w komentarzu bo w gridzie jest clock w metoda legenda

        # clock.tick(120)
        # timer = pg.time.get_ticks()

        grid.display_tilemap()
        # print(timer)

        # Player event
        agent.agent_move(grid.tilemap, grid.MAPWIDTH, grid.MAPHEIGHT)

        # player display
        agent.show_agent(grid.TILESIZE, grid.SURFACE)
        pg.display.update()


if __name__ == "__main__":
    main()
