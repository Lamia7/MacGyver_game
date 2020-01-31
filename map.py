#! /usr/bin/env python3
# coding: utf-8

from position import Position
import random
import config as conf
import pygame

class Map:
    """Class that contains the map and manages structure, random items positions"""

    def __init__(self):
        self.structure_map = [] #pr que meth get_play reconnaisse
        self.load_from_file()  #pr faire appel à load dès que j'appelle Map()

    def load_from_file(self):
        """Method that generates the map from the file that contains the level"""
        with open("level1.txt", "r") as file:  # ouvre fichier et ac with il le ferme
            #structure_map = []  # contient la liste principale
            for x, lines in enumerate(file):  # parcourt les lignes de la map
                lines_list = []  # stocke les lignes ds une liste de lignes
                for y, caract in enumerate(lines):  # parcourt les colonnes
                    if caract != '\n':
                        lines_list.append(caract)
                self.structure_map.append(lines_list)

            #return structure_map

    def display(self, window):
        """Method that displays the graphic part of the map"""
        walls = pygame.image.load(conf.WALLS).convert()
        start = pygame.image.load(conf.HERO).convert()
        arrival = pygame.image.load(conf.GUARDIAN).convert_alpha()


        line = 0
        for line_list in self.structure_map: #
            col = 0
            for caract in line_list:

                if caract == 'T':
                    window.blit(walls(Position, (line, col)))
                elif caract == 'S':
                    window.blit(start(Position, (line, col)))
                elif caract == 'A':
                    window.blit(arrival(Position, (line, col)))

                col += 1
            line += 1

        self.window.blit()
        pygame.display.flip()


        return Position(line, col)


    def get_player_start_pos(self):
        # se positionne en random dans un S
        line = 0
        col = 0
        for line_list in self.structure_map:
            for caract in line_list:
                if caract == 'S':
                    break
                else:
                    col = col +1
            line = line +1

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