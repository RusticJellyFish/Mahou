class TextWidget:

    def __init__(self, text):
        self.top  = 0
        self.left = 0
        self.height = len(text)
        self.text = text
        longestLine = 0
        for line in text:
            longestLine = max(longestLine, len(line))
        self.longestLine = longestLine

    def display(self, _screen, top, left):
        for lineNum in range(len(self.text)):
            line = self.text[lineNum]
            _screen.print_at(line, left, top + lineNum)
