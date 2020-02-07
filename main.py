#! /usr/bin/env python3
# coding: utf-8

"""Module that launches the game"""
import pygame
from map import Map
import config as conf
from hero import Hero

pygame.init()

#Displays window
window = pygame.display.set_mode((conf.WINDOW_SIZE, conf.WINDOW_SIZE))
#Displays title of window
pygame.display.set_caption("Macgyver Labyrinth Game")

main_loop = True

#Main loop
while main_loop:
    #Loads and displays homepage
    home = pygame.image.load(conf.HOME).convert()
    home = pygame.transform.scale(home, (conf.WINDOW_SIZE, conf.WINDOW_SIZE))
    window.blit(home, (0, 0)) #draws home image in window
    hero = pygame.image.load(conf.HERO).convert()

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

        pygame.display.flip()

    map = Map()
    map.load_from_file()
    hero = Hero(map.structure_map)

    #Game loop
    while game_loop:

        window.fill((0, 0, 0))

        # Speed loop limit
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_loop = False
                main_loop = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pass
                # Launches the map
                #map.display(window)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                hero.move('UP')
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                hero.move('DOWN')

        window.blit(map.paths, (0, 0))
        map.display(window)
        pygame.display.flip()
