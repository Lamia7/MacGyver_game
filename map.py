#! /usr/bin/env python3
# coding: utf-8

"""Module that handles the map with the characters and item positions"""
import hero
from position import Position
from item import Item
import random
import config as conf
#from hero import Hero
import pygame

class Map:
    """Class that contains the map and manages structure, random items positions"""

    def __init__(self):
        self.structure_map = []
        self.paths = pygame.image.load(conf.BACKGROUND).convert()
        self.items_list = []
        self.item_numbers = 3
        #self.get_item_position()
        self.x = 0
        self.y = 0
        self.load_from_file()  # pr faire appel à load dès que j'appelle Map()
        #self.create_items_list() #map appelle ici mes items
        self.items_positions = []  ##PQUOI?
        self.guardian_pos = 0


    def load_from_file(self):
        """Method that generates the map from the file that contains the level"""
        with open("level1.txt", "r") as file:  # ouvre fichier et ac with il le ferme à la fin
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
        self.paths = pygame.image.load(conf.BACKGROUND).convert()
        arrival = pygame.image.load(conf.GUARDIAN).convert_alpha()

        pygame.display.set_caption("Macgyver Labyrinth Game")


        #Displays images according to map structure and positions
        for y, line_list in enumerate(self.structure_map):  #

            for x, caract in enumerate(line_list):

                #print((x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE), y)
                if caract == 'T':
                    window.blit(walls, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
                elif caract == 'A':
                    self.guardian_pos = (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE)
                    window.blit(arrival, self.guardian_pos)
                else:
                    window.blit(self.paths, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
