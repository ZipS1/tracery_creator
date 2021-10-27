import pygame as pg


class ConsoleUI:
    def __init__(self):
        pass

    def input_size(self):
        is_valid = 0
        while is_valid == 0:
            print("\nInput size of tracery (x y): ", end="")
            inputted_size = input()

            is_valid = self._check_inputted_size(inputted_size)

        window = Window(inputted_size)
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
    def __init__(self, size_in_cells):
        pass

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
    console_ui = ConsoleUI()
    console_ui.input_size()


if __name__ == '__main__':
    main()
