import pygame as pg
from grid import Grid
from cell import Cell
from constants import *


class Window:
    def __init__(self, resolution, picture_size):
        self.resolution = resolution
        self.picture_size = picture_size
        self.cells = [Cell(x, y) for x in range(picture_size[0])
                                    for y in range(picture_size[1])]

        self.screen = pg.display.set_mode(resolution)
        pg.display.set_caption(WINDOW_TITLE)

        self.grid = Grid(self.screen, picture_size)

    def loop(self):
        clock = pg.time.Clock()
        run = True

        while run:
            clock.tick(FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

            self._draw_grid()
            self._draw_cells()

            pg.display.update()

    def _draw_grid(self):
        self.grid.draw_background()
        self.grid.draw_lines()

    def _draw_cells(self):
        for cell in self.cells:
            cell.draw()

    def _handle_click(self):
        pass

    def _save_picture(self):
        pass
