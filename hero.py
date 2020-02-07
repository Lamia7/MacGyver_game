#! /usr/bin/env python3
# coding: utf-8

from map import Map
from config import SPRITE_SIZE, NUMBER_SPRITE

class Hero:
    """This class manages the hero Macgyver"""

    def __init__(self, structure):  #position ou x et y?
        self.x = 0
        self.y = 0
        self.caract_x = 0
        self.caract_y = 0
        self.structure = structure


    def move(self, direction):
        """Method that manages player movements"""

        self.direction = direction
        #MOVE UP
        if direction == 'UP':
            if self.y > 0:
                if self.structure[self.caract_y - 1][self.caract_x] != 'm':
                    self.caract_y -= 1
                    self.y = self.caract_y * SPRITE_SIZE

        #MOVE DOWN
        if direction == 'DOWN':
            if self.structure[self.caract_y + 1][self.caract_x] != 'm':
                self.caract_y += 1
                self.y = self.caract_y * SPRITE_SIZE

