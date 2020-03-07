#! /usr/bin/env python3
# coding: utf-8

"""Module that launches the game"""
import pygame
from map import Map
import config as conf
from hero import Hero
from item import Item

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

    #Refresh
    pygame.display.flip()

    #Making these variables true at every loop
    game_loop = True
    home_loop = True
    win_page = False
    lost_page = False

    #Home loop that listens to events to know if game_loop starts or not
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

    #Initializing the map
    map = Map()
    map.display(window)

    #Initializing the hero
    hero_image = pygame.image.load(conf.HERO).convert()

    #Initializing the items
    images = [conf.needle, conf.ether, conf.tube]
    items_list = list()

    for img in images:
        item = Item(map, img)
        items_list.append(item)

    for item in items_list:
        print(f'{item.img} => x={item.random_x}, y={item.random_y}')
        pygame.display.flip()

    #Initializing the hero
    hero = Hero(map.structure_map)

    pygame.display.flip()

    #Game loop
    while game_loop:

        # Speed loop limit
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_loop = False
                main_loop = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                home_loop = False
                game_loop = True

            # Hero's movements with keyboard
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                hero.move('UP')
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                hero.move('DOWN')
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                hero.move('LEFT')
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                hero.move('RIGHT')

        window.blit(map.paths, (0, 0))
        map.display(window)

        # Displays items randomly
        for item in items_list:
            window.blit(item.img, (item.random_x, item.random_y))

        # Displays hero randomly
        window.blit(hero_image, (hero.x, hero.y))

        pygame.display.flip()

        # Removes item from items_list when hero passes over
        for item in items_list:
            if (item.random_x, item.random_y) == (hero.x, hero.y):
                items_list.remove(item)
                # Icrease the inventory every time hero collects an item
                hero.items_collected += 1
                print(hero.items_collected)

        # Win_game

        # When hero meets the guardian, game is over
        #PROBLEM
        if (hero.x, hero.y) == map.guardian_pos:

            # If hero has found all 3 items : he wins
            if hero.items_collected == 3:
                win_page = True

            # Lost_game
            else:
                # If hero 1 or more items missing : he looses
                if hero.items_collected < 3:
                    lost_page = True


            if win_page:
                #game_loop = False
                window = pygame.display.set_mode((conf.WINDOW_SIZE, conf.WINDOW_SIZE))
                pygame.display.set_caption("YAY! You did it!")
                end_page = pygame.image.load(conf.WIN_IMG).convert()
                #window.blit(conf.WIN_IMG, (0, 0))
                window.blit(pygame.transform.scale(end_page, (conf.WINDOW_SIZE, conf.WINDOW_SIZE)), (0, 0))

                pygame.display.flip()

            if lost_page:
                pygame.display.set_caption("Game over! You didn't find all the items...")
                window = pygame.display.set_mode((conf.WINDOW_SIZE, conf.WINDOW_SIZE))
                end_page = pygame.image.load(conf.GAME_OVER_IMG).convert()
                window.blit(pygame.transform.scale(end_page, (conf.WINDOW_SIZE, conf.WINDOW_SIZE)), (0, 0))

                pygame.display.flip()

            while lost_page or win_page:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        game_loop = False
                        main_loop = True
                        home_loop = True
                        lost_page = False
                        win_page = False
