import pygame as pg


WINDOW_TITLE = "Tracery Creator"
WINDOW_RESOLUTION = (800, 600)
PICTURE_SIZE = (10, 10)

FPS = 60

# cell states
BLANK = 0
UPSIDE_DIAGONAL = 1
DOWNSIDE_DIAGONAL = 2

# line states
BLANK = 0
FILLED = 1



class App:
    def __init__(self):
        pass

    def run(self):
        window = Window(WINDOW_RESOLUTION, PICTURE_SIZE)
        window.loop()


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


class Grid:
    def __init__(self, picture_size):
        pass

    def draw_background(self, resolution):
        pass

    def draw_lines(self, resolution):
        pass


class Line:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._state = BLANK

    def draw(self):
        pass

    def change_state(self):
        pass


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._state = BLANK

    def draw(self):
        pass

    def change_state(self):
        pass


def main():
    pg.init()

    app = App()
    app.run()

    pg.quit()


if __name__ == '__main__':
    main()
