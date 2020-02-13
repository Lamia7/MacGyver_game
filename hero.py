#! /usr/bin/env python3
# coding: utf-8

from map import Map
from config import SPRITE_SIZE, NUMBER_SPRITE
import pygame

class Hero:
    """This class manages the hero Macgyver"""

    def __init__(self, structure):  #position ou x et y?
        self.x = 0
        self.y = 0
        self.caract_x = 0
        self.caract_y = 0
        self.structure = structure
        #self.hero_img = pygame.image.load(HERO).convert_alpha()
        #self.position = ()
        #self.move()
        #self.rect = self.image.get_rect()


    def move(self, direction):
        """Method that manages player movements"""

        print("Direction {}".format(direction))
        self.direction = direction
        #MOVE UP
        if direction == 'UP':
            if self.caract_y > 0:
                if self.structure[self.caract_y - 1][self.caract_x] != 'T':
                    self.caract_y -= 1
                    self.y = self.caract_y * SPRITE_SIZE

        #MOVE DOWN
        if direction == 'DOWN':
            if self.caract_y < (NUMBER_SPRITE -1):
                if self.structure[self.caract_y + 1][self.caract_x] != 'T':
                    self.caract_y += 1
                    self.y = self.caract_y * SPRITE_SIZE

        #MOVE LEFT
        if direction == 'LEFT':
            if self.caract_x > 0:
                if self.structure[self.caract_y][self.caract_x-1] != 'T':
                    self.caract_x -= 1
                    self.x = self.caract_x * SPRITE_SIZE

        #MOVE RIGHT
        if direction == 'RIGHT':
            if self.caract_x < (NUMBER_SPRITE -1):
                if self.structure[self.caract_y][self.caract_x+1] != 'T':
                    self.caract_x += 1
                    self.x = self.caract_x * SPRITE_SIZE