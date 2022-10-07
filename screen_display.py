import colours
import pygame

#functions for drawing the screen
def draw_grid(screen,grid):
    blockSize = 25 #Set the size of the grid block
    for x in range(100, 800, blockSize):
        for y in range(100, 650, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, colours.BLACK, rect, 1)

            #draw coloured square
            if(grid[(x,y)] != None):
                rect = pygame.Rect(x+3,y+3,blockSize-6,blockSize-6)
                pygame.draw.rect(screen, grid[(x,y)],rect)

def draw_colour_choice(screen):
    x=910
    y=150
    width=44
    space=3
    border = pygame.Rect(x,y,width*6+space*7,width+space*2) 
    pygame.draw.rect(screen, colours.BLACK, border)
    

    for x_c in range(913,913+285,width):
        rect= pygame.Rect(x,)