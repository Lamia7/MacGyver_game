#! /usr/bin/env python3
# coding: utf-8

"""
    Item module that contains the Item class
"""

import random
from config import SPRITE_SIZE
import pygame

class Item:

    def __init__(self, my_map, img):
        """Constructor that initializes the items"""
        self.img = pygame.image.load(img).convert()
        self.random_x = ''
        self.random_y = ''
        self.map = my_map
        self.valid_positions = []
        self.get_valid_positions()
        self.set_position()

    def get_valid_positions(self):
        """Method that creates a list of valid positions"""

        for y, line in enumerate(self.map.structure_map):  # enum rec indice ds liste
            for x, caract in enumerate(line):
                if caract == 'o':  # 'o' is a valid path
                    self.valid_positions.append((x, y))

    def set_position(self):  # set car on met à jour
        """Method that sets a random position from the valid_positions list"""
        self.random_x, self.random_y = random.choice(self.valid_positions)

        self.random_x = self.random_x * SPRITE_SIZE
        self.random_y = self.random_y * SPRITE_SIZE

