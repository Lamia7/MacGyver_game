#! /usr/bin/env python3
# coding: utf-8

"""
    Hero module that contains the Hero class
"""

from config import SPRITE_SIZE, NUMBER_SPRITE


class Hero:
    """This class manages the hero Macgyver"""

    def __init__(self, structure):
        self.x = 0  # initial x position of the hero
        self.y = 0  # initial y position of the hero
        self.caract_x = 0  # new x position of the hero
        self.caract_y = 0  # new y position of the hero
        self.structure = structure
        self.items_collected = 0

    def move(self, direction):
        """Method that manages player movements"""

        # MOVE UP
        if direction == 'UP':
            if self.caract_y > 0:
                if self.structure[self.caract_y - 1][self.caract_x] != 'T':
                    self.caract_y -= 1
                    self.y = self.caract_y * SPRITE_SIZE

        # MOVE DOWN
        if direction == 'DOWN':
            if self.caract_y < (NUMBER_SPRITE - 1):
                if self.structure[self.caract_y + 1][self.caract_x] != 'T':
                    self.caract_y += 1
                    self.y = self.caract_y * SPRITE_SIZE

        # MOVE LEFT
        if direction == 'LEFT':
            if self.caract_x > 0:
                if self.structure[self.caract_y][self.caract_x-1] != 'T':
                    self.caract_x -= 1
                    self.x = self.caract_x * SPRITE_SIZE

        # MOVE RIGHT
        if direction == 'RIGHT':
            if self.caract_x < (NUMBER_SPRITE - 1):
                if self.structure[self.caract_y][self.caract_x+1] != 'T':
                    self.caract_x += 1
                    self.x = self.caract_x * SPRITE_SIZE
