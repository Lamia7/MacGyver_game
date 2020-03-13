#! /usr/bin/env python3
# coding: utf-8

"""
    Map module that contains the Map class
"""

import config as conf
import pygame


class Map:
    """Class that contains the map and manages structure, random items positions"""

    def __init__(self):
        self.structure_map = []
        self.paths = pygame.image.load(conf.BACKGROUND).convert()
        self.items_list = []
        self.item_numbers = 3
        self.x = 0
        self.y = 0
        self.load_from_file()  # pr faire appel à load dès que j'appelle Map()
        self.items_positions = []
        self.guardian_pos = 0

    def load_from_file(self):
        """Method that generates the map from the file that contains the level"""

        with open("level1.txt", "r") as file:  # opens the level1 file
            # structure_map = []  # contient la liste principale
            for lines in file:  # goes through lines in the file
                lines_list = []  # stores the lines in a lines' list variable
                for caract in lines:  # goes through sprites of each line
                    if caract != '\n':
                        lines_list.append(caract)

    def display(self, window):
        """Method that displays the graphic part of the map according to map structure and positions"""

        #  Loads the images
        walls = pygame.image.load(conf.WALLS).convert()
        self.paths = pygame.image.load(conf.PATHS).convert()
        arrival = pygame.image.load(conf.GUARDIAN).convert_alpha()

        pygame.display.set_caption(conf.MAIN_TITLE)


        # Displays images according to map structure and positions
        for y, line_list in enumerate(self.structure_map):

            for x, caract in enumerate(line_list):

                #print((x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE), y)
                if caract == 'T':
                    window.blit(walls, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
                elif caract == 'A':
                    self.guardian_pos = (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE)
                    window.blit(arrival, self.guardian_pos)
                else:
                    window.blit(self.paths, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
