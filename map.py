#! /usr/bin/env python3
# coding: utf-8

"""Module that handles the map with the characters and item positions"""

from position import Position
from item import Item
import random
import config as conf
import pygame

class Map:
    """Class that contains the map and manages structure, random items positions"""

    def __init__(self):
        self.structure_map = []  # pr que meth get_play reconnaisse
        self.load_from_file()  # pr faire appel à load dès que j'appelle Map()
        self.paths = pygame.image.load(conf.BACKGROUND).convert()
        self.paths = pygame.transform.scale(self.paths, (conf.SPRITE_SIZE, conf.SPRITE_SIZE))
        self.item_numbers = 3
        self.items_list = []
        #self.get_item_position()
        self.x = None
        self.y = None
        self.items_positions = []
        self.full_map = []

    def create_items_list(self):
        """Method that adds items in a list"""
        i = 0
        for i in range(0, self.item_numbers):
            self.items_list.insert(i, Item(self))

    def load_from_file(self):
        """Method that generates the map from the file that contains the level"""
        with open("level1.txt", "r") as file:  # ouvre fichier et ac with il le ferme
            # structure_map = []  # contient la liste principale
            for lines in file:  # parcourt les lignes de la map
                lines_list = []  # stocke les lignes ds une liste de lignes
                for caract in lines:  # parcourt les colonnes
                    if caract != '\n':
                        lines_list.append(caract)
                self.structure_map.append(lines_list)
            # return structure_map

    def display(self, window):
        """Method that displays the graphic part of the map"""
        walls = pygame.image.load(conf.WALLS).convert() #Loads the image
        walls = pygame.transform.scale(walls, (conf.SPRITE_SIZE, conf.SPRITE_SIZE)) #Resize image according to sprite size
        start = pygame.image.load(conf.HERO).convert()
        start = pygame.transform.scale(start, (conf.SPRITE_SIZE, conf.SPRITE_SIZE))
        self.paths = pygame.image.load(conf.BACKGROUND).convert()
        self.paths = pygame.transform.scale(self.paths, (conf.SPRITE_SIZE, conf.SPRITE_SIZE))
        arrival = pygame.image.load(conf.GUARDIAN).convert_alpha()
        arrival = pygame.transform.scale(arrival, (conf.SPRITE_SIZE, conf.SPRITE_SIZE))
        item0 = pygame.image.load(conf.ITEM0).convert()
        item0 = pygame.transform.scale(item0, (conf.SPRITE_SIZE, conf.SPRITE_SIZE))
        item1 = pygame.image.load(conf.ITEM1).convert()
        item1 = pygame.transform.scale(item1, (conf.SPRITE_SIZE, conf.SPRITE_SIZE))
        item2 = pygame.image.load(conf.ITEM2).convert()
        item2 = pygame.transform.scale(item2, (conf.SPRITE_SIZE, conf.SPRITE_SIZE))

        pygame.display.set_caption("Macgyver Labyrinth Game")

        #pygame.display.flip()

        #return window, background

        #Displays images according to map structure and positions
        for y, line_list in enumerate(self.structure_map):  #

            for x, caract in enumerate(line_list):
                #print((x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE), y)
                if caract == 'T':
                    window.blit(walls, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
                elif caract == 'S':
                    window.blit(start, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
                elif caract == 'A':
                    window.blit(arrival, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
                elif caract == "O0":
                    window.blit(item0, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
                elif caract == "O1":
                    window.blit(item1, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
                elif caract == "O2":
                    window.blit(item2, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
                else:
                    window.blit(self.paths, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))

                #col += 1
            #line += 1

            # self.window.blit()
            #pygame.display.flip()

        #return x, y

    def update_map(self, position):
        """Method that updates the map after the hero moves."""

    def get_player_start_pos(self):
        # se positionne en random dans un S
        line = 0
        col = 0
        for line_list in self.structure_map:
            for caract in line_list:
                if caract == 'S':
                    break
                else:
                    col = col + 1
            line = line + 1

        return Position(line, col)

    def add_items(self):
            line = 0
            col = 0
            valid_positions = []
            for line_list in self.structure_map:
                for caract in line_list:
                    if caract == 'o':
                        valid_positions.append(Position(line, col))
                    else:
                        col = col + 1
                line = line + 1
            return random.choice(valid_positions)

