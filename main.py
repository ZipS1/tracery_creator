import pygame as pg


WINDOW_TITLE = "Tracery Creator"
WINDOW_RESOLUTION = (800, 600)


class App:
    def __init__(self):
        pass

    def run(self):
        window = Window(WINDOW_RESOLUTION)
        window.loop()


class Window:
    def __init__(self, resolution):
        self.screen = pg.display.set_mode(resolution)
        pg.display.set_caption(WINDOW_TITLE)

    def loop(self):
        print("mainloop called...")

    def _draw_grid(self):
        pass

    def _draw_cell(self):
        pass

    def _handle_click(self):
        pass

    def _save_picture(self):
        pass


class Grid:
    def __init__(self):
        pass

    def _draw_layout(self):
        pass

    def _draw_line(self):
        pass


class Cell:
    def __init__(self):
        pass

    def _change_state(self):
        pass


def main():
    pg.init()

    app = App()
    app.run()

    pg.quit()


if __name__ == '__main__':
    main()
