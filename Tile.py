from asciimatics.screen import Screen

class Tile:

    def __init__(self, pos):
        self.pos = pos
        self.traversable = True
        self.char = "."
        self.color = Screen.COLOUR_WHITE
        self.visible = True
        self.timer = 0

    def display(self, _screen, col, row):
        myChar = self.char
        if not self.visible:
            myChar = " "
        _screen.print_at(myChar, col, row, self.color)

    def _update(self, delta):
        self.timer += delta
        if self.timer >= 1:
            self.timer -= 1
#            self.visible = not self.visible
