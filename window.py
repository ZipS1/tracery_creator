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
        self.margin_x = MARGIN_COEFFICIENT * self.width
        self.margin_y = MARGIN_COEFFICIENT * self.height

        self.screen = pg.display.set_mode(resolution)
        pg.display.set_caption(WINDOW_TITLE)

    def draw(self, cells, lines):
        self._draw_background()
        self._draw_lines()
        self._draw_cells()

    def _draw_background(self):
        self.screen.fill(WHITE)

    def _draw_lines(self):
        indent_x = round(self.margin_x + FILLED_LINE_WIDTH//2)
        indent_y = round(self.margin_y + FILLED_LINE_WIDTH//2)
        # TODO: make indents

    def _draw_cells(self):
        pass

    def get_clicked_object(self):
        pass
