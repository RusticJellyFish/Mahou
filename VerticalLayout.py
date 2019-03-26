class VerticalLayout:
    
    def __init__(self, top, left):
        self.top = top
        self.left = left
        self.panels = []
        
    def add_panel(self, panel):
        top = 0
        for p in self.panels:
            left += p.height
        panel.left = self.left
        panel.top = top
        
    def display(self, _screen):
        for panel in self.panels:
            panel.display(_screen)

