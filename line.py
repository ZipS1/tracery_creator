from constants import *


class Line:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = BLANK

    def draw(self):
        pass

    def change_state(self):
        pass
