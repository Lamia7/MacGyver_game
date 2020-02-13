from position import Position
import random

class Item:

    def __init__(self, structure_map):
        """init item"""

        self.random_x = ""
        self.random_y = ""
        self.i = ""
        #self.map = Map() non  car ca recrée
        self.structure = structure_map
        self.add_items()

    def add_items(self):
        """Method that randomly generates items in paths on the map"""
        i = True
        while i:
            random_x = random.randint(0, len(self.structure) - 1)
            random_y = random.randint(0, len(self.structure) -1)
            if self.structure[random_x][random_y] == "o":
                self.structure[random_x][random_y] = "I" + str(self.i)
                i = False

    def get_items_positions(self):
        items_position = (self.random_x, self.random_y)
        return items_position
