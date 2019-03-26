from asciimatics.screen import Screen

class Player:

    def __init__(self, pos):
        self.pos = pos
        self.char = "X"
        self.color = Screen.COLOUR_YELLOW

    def display(self, _screen, col, row):
        _screen.print_at(self.char, col, row, self.color)

    def tryMove(self, movement, m):
        newPos = [self.pos[0] + movement[0], self.pos[1] + movement[1]]
        if m.tiles[newPos[0]][newPos[1]].traversable:
            self.pos = newPos
