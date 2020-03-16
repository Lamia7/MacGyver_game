#! /usr/bin/env python3
# coding: utf-8

"""
Module that launches the game
"""

import pygame
from map import Map
import config as conf
from hero import Hero
from item import Item


class Game:
    """Class that launches the game"""

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.time.Clock().tick(30)  # Speed loop limit

        self.font_ka1 = pygame.font.Font('font/ka1.ttf', 25)
        self.home_page = True
        self.game_page = False
        self.final_page = False
        self.hero = ''

    def display_home_page(self):
        """Method that launches the game"""

        # Displays window
        window = pygame.display.set_mode((conf.MAZE_SIZE, conf.MAZE_SIZE))
        # Displays title of window
        pygame.display.set_caption(conf.MAIN_TITLE)

        # Loads and displays homepage
        home = pygame.image.load(conf.HOME).convert()
        home = pygame.transform.scale(home, (conf.MAZE_SIZE, conf.MAZE_SIZE))
        window.blit(home, (0, 0))  # Draws home image in window
        pygame.display.set_caption(conf.MAIN_TITLE)  # Title of the window

        # Refresh
        pygame.display.flip()

        # Home loop that listens to events to know if game_loop starts or not
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                    self.home_page = False
                    self.game_page = False
                    return False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.home_page = False
                    self.game_page = True
                    return False

    def display_game_page(self):

        window = pygame.display.set_mode((conf.MAZE_SIZE, (conf.MAZE_HEIGHT + conf.BANNER_HEIGHT)))
        pygame.display.set_caption(conf.MAIN_TITLE)  # Title of the window

        # Initializing the map
        maze = Map()
        maze.display(window)

        # Initializing the hero
        hero_image = pygame.image.load(conf.HERO).convert()

        # Initializing the items
        images = [conf.needle, conf.ether, conf.tube]
        items_list = list()

        for img in images:
            item = Item(maze, img)
            items_list.append(item)

        # Initializing the hero
        self.hero = Hero(maze.structure_map)

        pygame.display.flip()

        while True:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                    self.game_page = False
                    return False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.home_page = False
                    self.game_page = True
                    return False

                # Hero's movements with keyboard
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.hero.move('UP')
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.hero.move('DOWN')
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.hero.move('LEFT')
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.hero.move('RIGHT')

            window.blit(maze.paths, (0, 0))
            maze.display(window)

            # Displays items randomly
            for item in items_list:
                window.blit(item.img, (item.random_x, item.random_y))

            # Displays hero
            window.blit(hero_image, (self.hero.x, self.hero.y))

            # Bottom background
            banner = pygame.Surface((conf.MAZE_SIZE, conf.BANNER_HEIGHT))
            banner.fill((100, 100, 100))
            window.blit(banner, (0, conf.MAZE_HEIGHT))
            text = self.font_ka1.render(
                "Items recovered : " + str(self.hero.items_collected),
                1,
                (255, 255, 255))
            window.blit(text, (40, 500))

            pygame.display.flip()

            # Removes item from items_list when hero passes over
            for item in items_list:
                if (item.random_x, item.random_y) == (self.hero.x, self.hero.y):
                    items_list.remove(item)
                    # Increase the inventory every time hero collects an item
                    self.hero.items_collected += 1

            # ===========================
            # Winning or loosing the game
            # ===========================

            # When hero meets the guardian, game is over
            if (self.hero.x, self.hero.y) == maze.guardian_pos:
                self.final_page = True
                self.game_page = False
                return False

    def display_final_page(self):

        while True:

            # If hero has found all 3 items : MACGYVER WINS THE GAME
            if self.hero.items_collected == 3:
                window = pygame.display.set_mode((conf.MAZE_SIZE, conf.MAZE_SIZE))
                pygame.display.set_caption("YAY! You did it!")
                end_page = pygame.image.load(conf.WIN_IMG).convert()
                window.blit(pygame.transform.scale(end_page, (conf.MAZE_SIZE, conf.MAZE_SIZE)), (0, 0))

                pygame.display.flip()

                # If hero 1 or more items missing : MACGYVER LOOSES THE GAME
            elif self.hero.items_collected < 3:
                pygame.display.set_caption("Game over! You didn't find all the items...")
                window = pygame.display.set_mode((conf.MAZE_SIZE, conf.MAZE_SIZE))
                end_page = pygame.image.load(conf.GAME_OVER_IMG).convert()
                window.blit(pygame.transform.scale(end_page, (conf.MAZE_SIZE, conf.MAZE_SIZE)), (0, 0))

                pygame.display.flip()

            while self.final_page:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                        self.home_page = True
                        self.final_page = False
                        return False
