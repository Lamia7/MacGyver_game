import pygame
from map import Map
import config

pygame.init()

#Displays window
window = pygame.display.set_mode((700, 700))
#Displays title of window
pygame.display.set_caption("Macgyver Labyrinthe Game")

main_loop = True

#Main loop
while main_loop:
    #Loads and displays homepage
    home = pygame.image.load(config.HOME).convert()
    window.blit(home, (0,0)) #draws home image in window

    #Refresh
    pygame.display.flip()

    #Making these variables true at every loop
    game_loop = True
    home_loop = True

    #Home loop that listens if game_loop starts or not
    while home_loop:

        #Speed loop limit
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                home_loop = False
                game_loop = False
                main_loop = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                home_loop = False
                game_loop = True

    #Game loop
    while game_loop:

        # Speed loop limit
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_loop = False
                main_loop = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Launches the map
                map = Map()
                map.load_from_file()
                map.display(window)