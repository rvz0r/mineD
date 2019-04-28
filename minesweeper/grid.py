import random
import sys

import pygame as pg

class Grid:


    # display dimensions
    TILESIZE = 40
    MAPHEIGHT = 15
    MAPWIDTH = 15

    # colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # floors accessible
    GROUND = 0
    LANDMINE = 1

    # not accessible
    OBSTACLE = 2
    floor = [GROUND, LANDMINE, OBSTACLE]
    # dictionary linking textures with floors
    textures = {
        GROUND: pg.image.load('resources/ground.png'),
        OBSTACLE: pg.image.load('resources/obstacle.png'),
        LANDMINE: pg.image.load('resources/landmine.png')
    }
    # a list representing our tilemap
    tilemap = [[GROUND for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

    def generate_tilemap(self):
        # randomly generated flooring
        for rw in range(self.MAPHEIGHT):
            for cl in range(self.MAPWIDTH):
                num = random.randint(0, 15)
                if num < 10:
                    tile = self.GROUND
                elif 10 <= num < 13:
                    tile = self.OBSTACLE
                else:
                    tile = self.LANDMINE
                self.tilemap[rw][cl] = tile
                self.tilemap[0][0] = self.GROUND
