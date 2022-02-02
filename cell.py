from constants import *


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._state = BLANK

    def draw(self):
        pass

    def change_state(self):
        pass