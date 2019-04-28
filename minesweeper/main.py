import random

import pygame as pg

from minesweeper.agent import Player

# initializing PyGame module
pg.init()
print('This is our intelligent sprite running through a minefield!')





# creating a new drawing surface
SURFACE = pg.display.set_mode((TILESIZE*MAPWIDTH, TILESIZE*MAPHEIGHT + 50))
pg.display.set_caption('Minesweeper')
# mouse is not visible
pg.mouse.set_visible(False)
# creating a clock
clock = pg.time.Clock()
FPS = 120

# bar beneath the tilemap
TIME = 0
TILES = 0
MINES = 0

# font for legend
FONT = pg.font.Font(None, 40)

# legend bar
placePosition = 100
# clock legend
clock_image = pg.image.load('resources/clock.png')
SURFACE.blit(clock_image, (placePosition, MAPHEIGHT*TILESIZE + 5))
placePosition += 60
textObj1 = FONT.render(str(TIME), True, WHITE, BLACK)
SURFACE.blit(textObj1, (placePosition, MAPHEIGHT*TILESIZE + 13))
placePosition += 100
# tiles legend
feet = pg.image.load('resources/feet.png')
SURFACE.blit(feet, (placePosition, MAPHEIGHT*TILESIZE + 5))
placePosition += 56
textObj2 = FONT.render(str(TILES), True, WHITE, BLACK)
SURFACE.blit(textObj2, (placePosition, MAPHEIGHT*TILESIZE + 13))
placePosition += 100
# mines uncovered legend
mines = pg.image.load('resources/mines.png')
SURFACE.blit(mines, (placePosition, MAPHEIGHT*TILESIZE + 5))
placePosition += 60
textObj3 = FONT.render(str(MINES), True, WHITE, BLACK)
SURFACE.blit(textObj3, (placePosition, MAPHEIGHT*TILESIZE + 13))

# player object

playerPos = [0, 0]
PLAYER = pg.image.load("resources/agent.png").convert_alpha()
player = Player()






def main():
    # game loop
    while True:
        clock.tick(120)
        timer = pg.time.get_ticks()
        # print(timer)

        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                # pg.draw.rect(SURFACE, colors[tilemap[row][column]],
                # (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
                SURFACE.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))
        # Player event
        player.agent_move(tilemap, playerPos, MAPWIDTH, MAPHEIGHT)
        # player display
        player.show_agent(TILESIZE, SURFACE, PLAYER, playerPos)
        pg.display.update()


if __name__ == "__main__":
    generate_env()
    main()
