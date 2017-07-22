"""
A minesweeper game without a GUI.
"""
from random import sample


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



    width = min(4, max_width)
    height = min(1, max_height)
    number_of_mines = min(2, width * height - 1)
    return width, height, number_of_mines


def setup_game(width, height, number_of_mines):
    """Set up the 2-dimensional lists with mines and with the initial board to display"""
    # First, create 1-dimensional list of random mines
    random_mines = sample(range(width*height), number_of_mines)
    # translate the 1-dimensional list into a list with x,y coordinates for each mine
    mines = []
    for mine in random_mines:
        mines.append((mine % width, mine // width))
    board = []
    for x in range(width):
        board.append([])
        for y in range(height):
            board[x].append("~")
    return mines, board


def display_board():
    print('hello')
    pass


def get_move():
    pass


def main():
    width, height, number_of_mines = get_game_parameters()
    mines, board = setup_game(width, height, number_of_mines)



if __name__ == '__main__':
    main()
