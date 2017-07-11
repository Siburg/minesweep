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
    # translate the 1-dimensional list into a list with x,y coordinates for each mine
    for mine in set_mines:
        mines.append((mine % height, mine // height))
    board = []
    for x in range(width):
        board.append([])
        for y in range(height):
            board[x].append("o")
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
