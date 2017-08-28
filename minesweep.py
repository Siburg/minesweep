"""
A minesweeper game without a GUI.
"""
from random import sample
import os
import sys


def get_single_input(prompt, min_value, max_value):
    """Helper function to get an integer input one at a time."""
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


def get_game_parameters(max_width=76, max_height=20):
    """Get and validate size parameters for the game."""
    # Minimums are hard coded below. Could be included in parameters above,
    # or perhaps even defined as globals somehow, but seems unnecessary.
    MIN_WIDTH = 3
    MIN_HEIGHT = 3
    MIN_MINES = 1

    width = get_single_input('Enter width for the game board: ', MIN_WIDTH, max_width)
    height = get_single_input('Enter height for the game board: ', MIN_HEIGHT, max_height)
    print('Your game board has width of ' + str(width) + ' and height of ' + str(height) +
          ', providing ' + str(width * height) + ' locations to hide mines.')
    number_of_mines = get_single_input('Enter number of mines: ', MIN_MINES, width * height - 1)
    return width, height, number_of_mines


def setup_mines(width, height, number_of_mines):
    """Set up the 2-dimensional lists with mines.
    Output is mines in list of tuples with coordinates (x,y)"""
    # First, create 1-dimensional list of random mines
    random_mines = sample(range(width * height), number_of_mines)
    # translate the 1-dimensional list into a list with x,y coordinates for each mine
    mines = []
    for mine in random_mines:
        mines.append((mine % width, mine // width))
    return mines


def setup_board(width, height):
    """Set up the initial board to display. Output is board in 2-dimensional list form,
     with y as first sub-script and x as second subscript."""
    # 0 and positive numbers are later going to indicate cleared
    # values, so initialise it with negative numbers.
    board = []
    for y in range(height):
        board.append([])
        for x in range(width):
            board[y].append(-1)

    return board


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
            # negative numbers mean not yet cleared
            if board[y][x] < 0:
                print('#', end="")
            elif board[y][x] == 0:
                # Print middle dot (unicode) for zeros
                print('\u00B7', end="")
            else:
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


def reveal_board(mines, width, height):
    """Cheat function to reveal all mines and adjacent counts at any time.
    Mines will be indicated as 9's.
    This function does not change the actual board. Instead it sets up a
    temporary board and displays all the mines and surrounding counts on that."""
    reveal = setup_board(width, height)
    for x in range(width):
        for y in range(height):
            if (x, y) in mines:
                reveal[y][x] = 9
            else:
                reveal[y][x] = count_adjacent_mines((x, y), mines, width, height)

    display_board(reveal)
    return


def update_board(move, board, mines, width, height):
    """Updates the board after a move (after having already checked that we
    did not hit a mine). If there are any adjacent mines we display their count
    and are done. Otherwise, we run recursively in all directions until we
    encounter adjacent mines."""
    x = move[0]
    y = move[1]

    board[y][x] = count_adjacent_mines(move, mines, width, height)
    if board[y][x] > 0:
        return

    if x - 1 >= 0:
        update_board((x - 1, y), board, mines, width, height)
    #if x + 1 < width:
    #    update_board((x + 1, y), board, mines, width, height)
    """Problem is we can't run right and left, because that's endless loop I think"""

    if y - 1 >= 0:
        update_board((x, y - 1), board, mines, width, height)
    #if y + 1 < height:
    #    update_board((x, y + 1), board, mines, width, height)

    """
    if x + 1 < width:
        update_board((x + 1, y), board, mines, width, height)
        
        if y - 1 >= 0:
            update_board((x + 1, y - 1), board, mines, width, height)
        if y + 1 < height:
            update_board((x + 1, y + 1), board, mines, width, height)
        """
    return


def main():
    width, height, number_of_mines = get_game_parameters()
    mines = setup_mines(width, height, number_of_mines)
    board = setup_board(width, height)
    display_board(board)

    reveal_board(mines, width, height)

    move = get_move()

    if move in mines:
        print('You hit a mine. Game over.')
        sys.exit()

    update_board(move, board, mines, width, height)
    display_board(board)

    if sum(row.count(-1) for row in board) == number_of_mines:
        print('Congratulations, you have found all the mines. Game over.')
        sys.exit()


if __name__ == '__main__':
    main()
