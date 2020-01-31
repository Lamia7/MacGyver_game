from position import Position

class Item:
    def __init__(self, name, position=Position()):
        self.name = name
        self.position = position

item1 = Item("tube", Position(1,1)) #j'instancie Item, on modifiera plus tard la position