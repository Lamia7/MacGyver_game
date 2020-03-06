#! /usr/bin/env python3
# coding: utf-8

"""Module that handles the map with the characters and item positions"""
import hero
from position import Position
from item import Item
import random
import config as conf
# from hero import Hero
import pygame


class Map:
    """Class that contains the map and manages structure, random items positions"""

    def __init__(self):
        self.structure_map = []
        self.paths = pygame.image.load(conf.BACKGROUND).convert()
        self.items_list = []
        self.item_numbers = 3
        # self.get_item_position()
        self.x = 0
        self.y = 0
        self.load_from_file()  # pr faire appel à load dès que j'appelle Map()
        # self.create_items_list() #map appelle ici mes items
        self.items_positions = []  ##PQUOI?

    def create_items_list(self):
        """Method that adds items in a list"""

        for i in range(0, self.item_numbers):
            self.items_list.append(Item(self))  # Item(self) le self correspond à classe en cours (map)

    def check_items_positions(self):
        """Method that checks if position is already positioned"""

        items_positions = []  # liste vide de position d'items déjà positionés
        items_dict = {}
        for item in self.items_list:
            items_positions.append((item.random_x, item.random_y))  # accède à attribut de l'obj
            # while (item.random_x, item.random_y) not in item_positions:  # si position pas déjà prise
            if item > 0:
                while items_positions[item - 1] == (item.random_x, item.random_y):
                    item.set_position()
                    # print(items_positions)
                    items_dict[item.obj1, item.obj2, item.obj3] = item.set_position()
                    # print(items_positions)
                    return items_dict
                    # print(items_dictionary)
            # item.get_valid_positions()
            # items_positions.append((item.random_x, item.random_y))

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

        walls = pygame.image.load(conf.WALLS).convert()  # Loads the image
        self.paths = pygame.image.load(conf.BACKGROUND).convert()
        arrival = pygame.image.load(conf.GUARDIAN).convert_alpha()

        pygame.display.set_caption("Macgyver Labyrinth Game")

        # Displays images according to map structure and positions
        for y, line_list in enumerate(self.structure_map):  #

            for x, caract in enumerate(line_list):

                # print((x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE), y)
                if caract == 'T':
                    window.blit(walls, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
                elif caract == 'A':
                    window.blit(arrival, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
                else:
                    window.blit(self.paths, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))

                # col += 1
            # line += 1

            # self.window.blit()
            # pygame.display.flip()

        # return x, y

    # def update_map(self, position):
    # """Method that updates the map after the hero moves."""


"""




    def create_items_list(self):
        #Method that adds items in a list

        for i in range(self.item_numbers):
            self.items_list.append(Item(self, conf.needle, conf.ether, conf.tube))  # Item(self) le self correspond à classe en cours (map)

            #return self.items_list

        for n in range(len(self.items_list)):
            items = Item(self.items_list[n])
            if n > 0:
                while self.items_positions[n-1] == (items.random_x, items.random_y):
                    items.set_position()
                self.items_positions.append((items.random_x, items.random_y))
        print(self.items_list)



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


    def item_counter(self, news_x, news_y):
        if self.structure_map[news_x][news_y] in ("I0", "I1", "I2"):
            self.hero.items_collect += 1
            self.structure_map[news_x][news_y] = "o"
            """

