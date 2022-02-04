import pygame as pg
from constants import *


class Window:
    """
    Responsible for showing app window on the screen,
    and preprocess clicks on the screen,
    found out what object user clicked on
    """
    def __init__(self, resolution, picture_size):
        self.width, self.height = resolution
        self.cells_on_x, self.cells_on_y = picture_size

        self.screen = pg.display.set_mode(resolution)
        pg.display.set_caption(WINDOW_TITLE)

    def draw(self, cells, lines):
        self._draw_background()
        self._draw_lines()

    def _draw_background(self):
        self.screen.fill(WHITE)

    def _draw_lines(self):
        for x in range(0, self.width + 1, round(self.width/self.cells_on_x)):
            pg.draw.line(
                self.screen, BLANK_LINE_COLOR,
                (x, 0), (x, self.height), width=3)

        for y in range(0, self.height + 1, round(self.height/self.cells_on_y)):
            pg.draw.line(
                self.screen, BLANK_LINE_COLOR,
                (0, y), (self.width, y), width=3)

    def _draw_cells(self):
        pass

    def get_clicked_object(self):
        pass
