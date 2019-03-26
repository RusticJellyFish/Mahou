class Panel:

    def __init__(self, top, left, height, width):
        self.top  = top
        self.left = left
        self.height = height
        self.width  = width
        self.widget = None

    def set_widget(self, widget):
        sef.widget = widget

    def display(self, _screen):
        self.widget.display(_screen, self.top, self.left)
