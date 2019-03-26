from Tile import Tile
from asciimatics.screen import Screen
from random import randint

class FloorTile(Tile):

    def __init__(self, pos):
        super().__init__(pos)
        self.char = "."
