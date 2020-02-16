from position import Position
import random
from config import SPRITE_SIZE

class Item:

    def __init__(self, my_map, i=""):
        """init item"""

        self.random_x = ""
        self.random_y = ""
        self.i = i
        #self.map = Map() non  car ca recrée
        #self.structure = structure_map
        #self.add_items()
        self.url = ""
        #self.get_items_positions()
        self.map = my_map

    def add_items(self):
        """Method that randomly generates items in paths on the map"""
        #self.structure = structure_map

        i = True
        while i:
            random_x = random.randint(0, self.map.x)
            random_y = random.randint(0, self.map.y)
            if self.map.structure_map[random_x][random_y] == "o":
                self.map.structure_map[random_x][random_y] = "I" + str(self.i)
                i = False

"""    def get_items_positions(self):
        items_position = (self.random_x * SPRITE_SIZE, self.random_y * SPRITE_SIZE)
        return items_position"""


"""    def add_items(self, structure_map):       
        self.structure = structure_map

        i = True
        while i:
random_x = random.randint(0, len(self.structure) - 1)
random_y = random.randint(1, len(self.structure[0]) - 2)"""