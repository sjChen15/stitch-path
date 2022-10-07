import pygame

#defined functions
import colours
from screen_display import draw_colour_choice, draw_grid
from grid_control import init_grid
#game init
pygame.init()
size = (1300, 750)
SCREEN = pygame.display.set_mode(size)
pygame.display.set_caption("Stitch Path")
carryOn = True
clock = pygame.time.Clock()

#grid init

grid = init_grid()
grid[(200,500)] = colours.RED

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we can exit the while loop
 
    # --- Game logic


    # --- Drawing code
    SCREEN.fill(colours.WHITE) # First, clear the screen to white. 
    draw_grid(SCREEN,grid) #draw the grid
    draw_colour_choice(SCREEN)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()