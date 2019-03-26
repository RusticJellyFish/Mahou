from Tile import Tile
from asciimatics.screen import Screen

class WallTile(Tile):

    def __init__(self, pos):
        super().__init__(pos)
        self.traversable = False
        self.char = '#'
        self.color = 10
