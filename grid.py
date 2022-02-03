import pygame as pg
from constants import *


class Grid:
    def __init__(self, screen, picture_size):
        self.screen = screen
        self.picture_size = picture_size

    def draw_background(self):
        width, height = self.screen.get_size()
        cells_in_width, cells_in_height = self.picture_size
        self.screen.fill(WHITE)

        for x in range(0, width + 1, round(width/cells_in_width)):
            pg.draw.line(self.screen, BLANK_LINE_COLOR, (x, 0), (x, height), width=3)

        for y in range(0, height + 1, round(height/cells_in_height)):
            pg.draw.line(self.screen, BLANK_LINE_COLOR, (0, y), (width, y), width=3)


    def draw_lines(self):
        pass
