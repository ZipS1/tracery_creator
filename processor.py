import pygame as pg
from window import Window
from cell import Cell
from line import Line
from constants import *


class Processor:
    """
    Responsible for processing of inner procedures.
    Central class.
    """
    def __init__(self, resolution, picture_size):
        self.resolution = resolution
        self.picture_size = cells_in_width, cells_in_height = picture_size
        self.window = Window(resolution, picture_size)

        self.cells = [[Cell() for x in range(cells_in_width)]
                                for x in range(cells_in_height)]
        self.lines = [[Line() for x in range(cells_in_width + 1)]
                                for y in range(cells_in_height + 1)]

    def loop(self):
        clock = pg.time.Clock()
        run = True

        while run:
            clock.tick(FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

            self.window.draw(self.cells, self.lines)

            pg.display.update()

    def _save_picture(self):
        pass

