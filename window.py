import pygame as pg
from grid import Grid
from cell import Cell
from constants import *


class Window:
    def __init__(self, resolution, picture_size):
        self._resolution = resolution
        self._picture_size = picture_size
        self._cells = [Cell(x, y) for x in range(picture_size[0])
                                    for y in range(picture_size[1])]

        self.screen = pg.display.set_mode(resolution)
        pg.display.set_caption(WINDOW_TITLE)

        grid = Grid(picture_size)

    def loop(self):
        clock = pg.time.Clock()

        run = True
        while run:
            clock.tick(FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

    def _draw_grid(self):
        self.grid.draw_background(self._resolution)
        self.grid.draw_lines(self._resolution)

    def _draw_cells(self):
        for cell in self._cells:
            cell.draw()

    def _handle_click(self):
        pass

    def _save_picture(self):
        pass
