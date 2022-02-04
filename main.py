import pygame as pg
from processor import Processor
from constants import *


class App:
    """
    Class which runs main loop and making preparatory procedures before
    running this main loop
    """
    def __init__(self):
        pass

    def run(self):
        processor = Processor(WINDOW_RESOLUTION, PICTURE_SIZE)
        processor.loop()


def main():
    pg.init()

    app = App()
    app.run()

    pg.quit()


if __name__ == '__main__':
    main()
