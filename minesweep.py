"""
A minesweeper game without a GUI.
"""

def get_game_parameters(max_width=76, max_height=20):
    width = min(2, max_width)
    height = min(1, max_height)
    number_of_mines = min(2, width * height - 1)
    return width, height, number_of_mines


def setup_game():
    pass


def display_board():
    print('hello')
    pass


def get_move():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
