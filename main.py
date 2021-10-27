import pygame as pg


CELL_SIZE = 50                      # size of cell in pixels
GRID_WIDTH = 5                      # grid width in pixels
WINDOW_TITLE = "Tracery Creator"


class ConsoleUI:
    def __init__(self):
        pass

    def input_size(self):
        is_valid = 0
        while is_valid == 0:
            print("\nInput size of tracery (x y): ", end="")
            inputted_size = input()

            is_valid = self._check_inputted_size(inputted_size)

        field_size = list(map(int, inputted_size.split()))
        window = Window(field_size)
        window.mainloop()

    def _check_inputted_size(self, user_input):
        is_valid = 0
        user_input = user_input.split()

        match user_input:
            case x, y:
                if x.isdigit() and y.isdigit():
                    is_valid = 1
                else:
                    print("Incorrect input!")
            case _:
                print("Incorrect input!")

        return is_valid


class Window:
    def __init__(self, field_size):
        self.screen = pg.display.set_mode(field_size)
        pg.display.set_caption(WINDOW_TITLE)

    def mainloop(self):
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

    console_ui = ConsoleUI()
    console_ui.input_size()

    pg.quit()


if __name__ == '__main__':
    main()
