"""
A minesweeper game without a GUI.
"""
from random import sample
import os
import sys


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
    """Set up the 2-dimensional lists with mines and with the initial board to display.
    Output is mines in list of tuples with coordinates (x,y), and
    board in form 2-dimensional list form, with y as dimension 1 and x as dimension 2"""
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
    def print_x_coordinate_singles(widthp1):
        print('  x|', end="")
        for xp1 in range(1, widthp1):
            print(xp1 % 10, end="")
        print('|')

    def print_x_coordinate_tens(widthp1):
        print('   |', end="")
        for xp1 in range(1, widthp1):
            if xp1 % 10 == 0:
                print(xp1 // 10, end="")
            else:
                print(' ', end="")
        print('|')

    os.system('clear')
    print_x_coordinate_tens(len(board[0]) + 1)
    print_x_coordinate_singles(len(board[0]) + 1)
    print('-' * (len(board[0])+7))

    for y in range(len(board) - 1, -1, -1):
        print('y{0:2}|'.format(y + 1), end="")
        for x in range(len(board[0])):
            print(board[y][x], end="")
        print('|{0:2}y'.format(y + 1))

    print('-' * (len(board[0])+7))
    print_x_coordinate_singles(len(board[0]) + 1)
    print_x_coordinate_tens(len(board[0]) + 1)


def get_move():
    """Gets player input, without validation or checks, and returns tuple
    with x and y coordinate for computer; i.e. human entry - 1"""
    move = input('Enter x and y coordinates for next move, separated by space; or  q  to exit: ')
    if move.lower() == 'q':
        print('Thanks for playing; exiting program now.')
        sys.exit()
    move = move.split()
    return int(move[0]) - 1, int(move[1]) - 1


def count_adjacent_mines(move, mines, width, height):
    """Counts number of mines immediately adjacent to the coordinates of a move"""
    count = 0
    x = move[0]
    y = move[1]

    # Statement below does redundant check for x,y as well
    # (we already checked that's not a mine) but so be it.
    # Note we want to check for x+1 and y+1, so range stops at x+2 and y+2;
    # unless we reach edge of board earlier
    for ix in range(max(0, x - 1), min(width, x + 2)):
        for iy in range(max(0, y - 1), min(height, y + 2)):
            if (ix, iy) in mines:
                count += 1

    return count


def main():
    width, height, number_of_mines = get_game_parameters()
    mines, board = setup_game(width, height, number_of_mines)
    display_board(board)
    print(mines)
    for x in range(width):
        for y in range(height):
            if (x, y) in mines:
                board[y][x] = '*'
            else:
                count = count_adjacent_mines((x, y), mines, width, height)
                if count > 0:
                    board[y][x] = count
                else:
                    board[y][x] = ' '

    display_board(board)

"""
    move = get_move()
    if move in mines:
        print('You hit a mine. Game over.')
        sys.exit()
"""

if __name__ == '__main__':
    main()
