#! /usr/bin/env python3
# coding: utf-8

from position import Position
import random
from config import SPRITE_SIZE, NUMBER_SPRITE
import pygame
import config as conf


class Item:

    # items = [] pr ne pas ajouter ds main les 3 créations d'item ac append, un par un

    def __init__(self, my_map, item1, item2, item3):
        """init item"""

        self.random_x = ''  # ""
        self.random_y = ''  # ""
        # self.items = []
        #self.items = {}
        #for item, image in conf.items():
            #self.items[item] = pygame.image.load(image).convert()
            #self.items[item] = pygame.transform.scale(self.items[image], (SPRITE_SIZE, SPRITE_SIZE))
        #for item in conf.items:
        self.obj1 = pygame.image.load(item1).convert()
        self.obj1 = pygame.transform.scale(self.obj1, (SPRITE_SIZE, SPRITE_SIZE))
        self.obj2 = pygame.image.load(item2).convert()
        self.obj2 = pygame.transform.scale(self.obj2, (SPRITE_SIZE, SPRITE_SIZE))
        self.obj3 = pygame.image.load(item3).convert()
        self.obj3 = pygame.transform.scale(self.obj3, (SPRITE_SIZE, SPRITE_SIZE))
        # self.get_items_positions()
        self.map = my_map
        # self.add_items()
        # Item.items.append(self) #s'auto ajoute à la liste items
        #self.img = pygame.image.load(conf.ITEM0).convert()
        #self.img = pygame.transform.scale(self.img, (SPRITE_SIZE, SPRITE_SIZE))
        self.valid_positions = []
        self.get_valid_positions()
        self.set_position()
        #self.show = True

        # if 'needle'
        # item0 = pygame.image.load(conf.ITEM0).convert()
        # item0 = pygame.transform.scale(item0, (conf.SPRITE_SIZE, conf.SPRITE_SIZE))

    def get_valid_positions(self):
        """Method that creates a list of valid positions"""
        # self.structure = structure_map

        # valid_positions = []
        for y, line in enumerate(self.map.structure_map):  # enum rec indice ds liste
            for x, caract in enumerate(line):
                if caract == 'o':
                    self.valid_positions.append((x, y))

    def set_position(self):  # set car on met à jour
        """Method that sets a random position from the valid_positions list"""
        self.random_x, self.random_y = random.choice(self.valid_positions)

        self.random_x = self.random_x * SPRITE_SIZE
        self.random_y = self.random_y * SPRITE_SIZE


"""    
        position = (self.random_x * SPRITE_SIZE, self.random_y * SPRITE_SIZE)
        return position
        
        def add_items(self, structure_map):       
        self.structure = structure_map

        i = True
        while i:
random_x = random.randint(0, len(self.structure) - 1)
random_y = random.randint(1, len(self.structure[0]) - 2)

    def add_items(self):

        while True:
            random_x = random.randint(0, self.map.structure_map.x)
            random_y = random.randint(0, self.map.structure_map.y)
            if self.map.structure_map[random_x][random_y] == "o":
                self.map.structure_map[random_x][random_y] = "I" + str(self.i)
                break
                
                
        while True:
            self.random_x, self.random_y = random.choice(valid_positions)
            item_positions = []  #liste de position d'items déjà positionés
            for item in self.items:
                item_positions.append((item.random_x, item.random_y))  #accède à attribut de l'obj
            if (self.random_x, self.random_y) not in item_positions:  #si position pas déjà prise
                break       """
