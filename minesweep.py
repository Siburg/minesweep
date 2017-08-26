"""
A minesweeper game without a GUI.
"""
from random import sample
import os


def get_game_parameters(max_width=76, max_height=20):
    """Get and validate size parameters for the game."""
    # Minimums are hard coded below. Could be included in parameters above,
    # or perhaps even defined as globals somehow, but seems unnecessary.
    MIN_WIDTH = 3
    MIN_HEIGHT = 3
    MIN_MINES = 1

    def get_single_input(prompt, min_value, max_value):
        """Helper function to get each input one at a time."""
        while True:
            try:
                entry = int(input(prompt))
                if entry < min_value or entry > max_value:
                    print('You entered a number outside the allowed range! ' +
                          'The number needs to be at least ' + str(min_value) +
                          ' and no larger than ' + str(max_value) +
                          '. Please try again.')
                else:
                    return entry
            except TypeError:
                print('You should have entered a number. Please try again.')

    width = get_single_input('Enter width for the game board: ', MIN_WIDTH, max_width)
    height = get_single_input('Enter height for the game board: ', MIN_HEIGHT, max_height)
    print('Your game board has width of ' + str(width) + ' and height of ' + str(height) +
          ', providing ' + str(width * height) + ' locations to hide mines.')
    number_of_mines = get_single_input('Enter number of mines: ', MIN_MINES, width * height - 1)
    return width, height, number_of_mines


def setup_game(width, height, number_of_mines):
    """Set up the 2-dimensional lists with mines and with the initial board to display"""
    # First, create 1-dimensional list of random mines
    random_mines = sample(range(width * height), number_of_mines)
    # translate the 1-dimensional list into a list with x,y coordinates for each mine
    mines = []
    for mine in random_mines:
        mines.append((mine % width, mine // width))
    board = []
    for y in range(height):
        board.append([])
        for x in range(width):
            board[y].append('~')
    return mines, board


def display_board(board):
    """Print the board with x and y axis in human counting form."""
    os.system('clear')
    print('   |', end="")
    for xp1 in range(1, len(board[0]) + 1):
        if xp1 % 10 == 0:
            print(xp1 // 10, end="")
        else:
            print(' ', end="")
    print('|')

    print('  x|', end="")
    for xp1 in range(1, len(board[0]) + 1):
        print(xp1 % 10, end="")
    print('|')

    print('-' * (len(board[0])+7))

    for y in range(len(board) - 1, -1, -1):
        print('y{0:2}|'.format(y + 1), end="")
        for x in range(len(board[0])):
            print(board[y][x], end="")
        print('|{0:2}y'.format(y + 1))

    print('-' * (len(board[0])+7))
    print('  x|', end="")
    for xp1 in range(1, len(board[0]) + 1):
        print(xp1 % 10, end="")
    print('|')

    print('   |', end="")
    for xp1 in range(1, len(board[0]) + 1):
        if xp1 % 10 == 0:
            print(xp1 // 10, end="")
        else:
            print(' ', end="")
    print('|')

def get_move():
    pass


def main():
    width, height, number_of_mines = get_game_parameters()
    mines, board = setup_game(width, height, number_of_mines)
    display_board(board)

if __name__ == '__main__':
    main()
