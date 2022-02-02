import pygame as pg
from window import Window
from constants import *

class App:
    def __init__(self):
        pass

    def run(self):
        window = Window(WINDOW_RESOLUTION, PICTURE_SIZE)
        window.loop()


def main():
    pg.init()

    app = App()
    app.run()

    pg.quit()


if __name__ == '__main__':
    main()
