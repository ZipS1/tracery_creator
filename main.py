import pygame as pg


class ConsoleUI:
    def __init__(self):
        pass

    def input_size(self):
        print("Input size of tracery (x y): ", end="")
        tracery_size = map(int, input().split())

        # add match construction here to check input

        window = Window(tracery_size)
        window.mainloop()


class Window:
    def __init__(self, size_in_cells):
        pass

    def mainloop(self):
        pass

    def draw_grid(self):
        pass

    def draw_cell(self):
        pass

    def handle_click(self):
        pass

    def save_picture(self):
        pass


class Grid:
    def __init__(self):
        pass

    def draw_layout(self):
        pass

    def draw_line(self):
        pass


class Cell:
    def __init__(self):
        pass

    def change_state(self):
        pass


def main():
    console_ui = ConsoleUI()
    console_ui.input_size()


if __name__ == '__main__':
    main()
