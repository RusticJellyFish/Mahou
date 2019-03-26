class HorizontalLayout:

    def __init__(self, top, left):
        self.top = top
        self.left = left
        self.panels = []

    def add_panel(self, panel):
        left = 0
        for p in self.panels:
            left += p.width
        panel.top = self.top
        panel.left = left
        self.panels.append(panel)

    def display(self, _screen):
        for panel in self.panels:
            panel.display(_screen)
