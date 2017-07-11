"""
A minesweeper game without a GUI.
"""
from random import sample


def get_game_parameters(max_width=76, max_height=20):
    width = min(2, max_width)
    height = min(1, max_height)
    number_of_mines = min(2, width * height - 1)
    return width, height, number_of_mines


def setup_game(width, height, number_of_mines):
    """Set up the 2-dimensional lists with mines and with the initial board to display"""
    # First, create 1-dimensional list of random mines
    set_mines = sample(range(width*height), number_of_mines)
    mines = []
    board = []
    for x in range(width):
        mines.append([])
        board.append([])
        for y in range(height):
            mines[x].append(False)
            board[x].append("o")
    # note we have not yet done anything to indicate where are mines actually are
    return mines, board


def display_board():
    print('hello')
    pass


def get_move():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
