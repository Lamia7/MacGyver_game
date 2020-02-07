#! /usr/bin/env python3
# coding: utf-8

"""Module that handles the map with the characters and item positions"""

from position import Position
import random
import config as conf
import pygame


class Map:
    """Class that contains the map and manages structure, random items positions"""

    def __init__(self):
        self.structure_map = []  # pr que meth get_play reconnaisse
        self.load_from_file()  # pr faire appel à load dès que j'appelle Map()

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
        #Loads image
        walls = pygame.image.load(conf.WALLS).convert()
        #Resize image according to sprite size
        walls = pygame.transform.scale(walls, (conf.SPRITE_SIZE, conf.SPRITE_SIZE))
        start = pygame.image.load(conf.HERO).convert()
        start = pygame.transform.scale(start, (conf.SPRITE_SIZE, conf.SPRITE_SIZE))
        paths = pygame.image.load(conf.BACKGROUND).convert()
        paths = pygame.transform.scale(paths, (conf.SPRITE_SIZE, conf.SPRITE_SIZE))
        arrival = pygame.image.load(conf.GUARDIAN).convert_alpha()
        arrival = pygame.transform.scale(arrival, (conf.SPRITE_SIZE, conf.SPRITE_SIZE))

        pygame.display.set_caption("Macgyver Labyrinth Game")

        pygame.display.flip()

        #return window, background

        #line = 0
        for y, line_list in enumerate(self.structure_map):  #
            #col = 0
            for x, caract in enumerate(line_list):
                print((x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE), y)
                if caract == 'T':
                    window.blit(walls, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
                elif caract == 'S':
                    window.blit(start, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
                elif caract == 'A':
                    window.blit(arrival, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))
                else:
                    window.blit(paths, (x * conf.SPRITE_SIZE, y * conf.SPRITE_SIZE))

                #col += 1
            #line += 1

            # self.window.blit()
            pygame.display.flip()

        return x, y


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


def get_item_position(self):
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
