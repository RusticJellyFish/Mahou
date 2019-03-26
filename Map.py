import random

from asciimatics.screen import Screen
from Tile import Tile
from WallTile import WallTile
from FloorTile import FloorTile

class Map:

    def __init__(self, height, width, displayHeight, displayWidth, freeHeight, freeWidth):
        self.width  = width
        self.height = height
        self.tiles = self.rand_map()

        self.displayHeight = displayHeight
        self.displayWidth  = displayWidth

        self.freeHeight = displayHeight // 2 - freeHeight
        self.freeWidth  = displayWidth  // 2 - freeWidth

        self.topDisplay  = 0
        self.leftDisplay = 0

        self.player = None

    def rand_map(self):
        tiles = []
        for w in range(self.width):
            tiles.append([])
            for h in range(self.height):
                if self.is_border(w, h) or random.random() < .2:
                    tiles[w].append(WallTile([w,h]))
                else:
                    tiles[w].append(FloorTile([w,h]))
        return tiles
    def is_border(self, w, h):
        return w == 0 or h == 0 or w == self.width-1 or h == self.height - 1
    def output_map(self):
        for col in self.tiles:
            colOutput = ""
            for tile in col:
                colOutput += tile
            print(colOutput)

    def set_player(self, player):
        self.player = player

    def center_on_player(self, player):
        self.topDisplay  = max(0, player.pos[1] - self.displayHeight // 2)
        self.leftDisplay = max(0, player.pos[0] - self.displayWidth  // 2)
        self.freePos     = [player.pos[0], player.pos[1]]

    def on_player_movement(self, player):
        if self.freePos[1] - player.pos[1] > self.freeHeight:
            if self.topDisplay > 0:
                self.topDisplay = self.topDisplay - 1
                self.freePos[1] = self.freePos[1] - 1
        if player.pos[1] - self.freePos[1] > self.freeHeight:
            if self.topDisplay < self.height - self.displayHeight:
                self.topDisplay = self.topDisplay + 1
                self.freePos[1] = self.freePos[1] + 1
        if player.pos[0] - self.freePos[0] > self.freeWidth:
            if self.leftDisplay < self.width - self.displayWidth:
                self.leftDisplay = self.leftDisplay + 1
                self.freePos[0] = self.freePos[0] + 1
        if self.freePos[0] - player.pos[0] > self.freeWidth:
            if self.leftDisplay > 0:
                self.leftDisplay = self.leftDisplay - 1
                self.freePos[0] = self.freePos[0] - 1


    def display(self, _screen, top, left):
        for h in range(self.displayHeight):
            for w in range(self.displayWidth):
                row = h + self.topDisplay
                col = w + self.leftDisplay
                tile = self.tiles[col][row]
                tile.display(_screen, 2 * (w + left), top + h)
        playerCol = 2 * (self.player.pos[0] - self.leftDisplay + left)
        playerRow = self.player.pos[1] - self.topDisplay + top
        self.player.display(_screen, playerCol, playerRow)



def demo(_screen):
    m = Map(10, 10)

    while True:
        for row in range(m.height):
            #rowOutput = ""
            for col in range(m.width):
                #rowOutput += m.tiles[col][row]
                _screen.print_at(m.tiles[col][row].char, 2 * col, row, tile.color)
                if col < m.width:
                    _screen.print_at(' ', 2 * col + 1, row)
        ev = _screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        _screen.refresh()

#Screen.wrapper(demo)
