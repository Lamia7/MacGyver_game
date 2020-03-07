#! /usr/bin/env python3
# coding: utf-8

from position import Position
import random
from config import SPRITE_SIZE, NUMBER_SPRITE
import pygame
import config as conf


class Item:

    # items = [] pr ne pas ajouter ds main les 3 créations d'item ac append, un par un

    def __init__(self, my_map, img):
        """init item"""
        self.img = pygame.image.load(img).convert()
        self.random_x = ''
        self.random_y = ''
        self.map = my_map
        self.valid_positions = []
        self.get_valid_positions()
        self.set_position()
        #self.obj2 = pygame.image.load(conf.ether).convert()
        #self.obj3 = pygame.image.load(conf.tube).convert()


    def get_valid_positions(self):
        """Method that creates a list of valid positions"""

        for y, line in enumerate(self.map.structure_map):  # enum rec indice ds liste
            for x, caract in enumerate(line):
                if caract == 'o':
                    self.valid_positions.append((x, y))

    def set_position(self):  # set car on met à jour
        """Method that sets a random position from the valid_positions list"""
        self.random_x, self.random_y = random.choice(self.valid_positions)

        self.random_x = self.random_x * SPRITE_SIZE
        self.random_y = self.random_y * SPRITE_SIZE

