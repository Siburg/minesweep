"""unit tests for minesweep.py"""

import minesweep
import unittest
from unittest import mock
#import sys
#import io


class TestGetSingleInput(unittest.TestCase):
    """ test function get_single_input"""

    def setUp(self):
        self.prompt = 'spam'
        self.min_value = 1
        self.max_value = 99

    def test_returned_entry_is_integer(self):
        """check that we get an integer value as return"""
        with mock.patch('builtins.input', side_effect=('9')):
            entry = minesweep.get_single_input(self.prompt, self.min_value, self. max_value)
        self.assertEqual(type(entry), int)

    def test_returned_entry_equals_entry(self):
        """check that the return value is integer value of entry"""
        with mock.patch('builtins.input', side_effect=('9')):
            entry = minesweep.get_single_input(self.prompt, self.min_value, self.max_value)
        self.assertEqual(entry, 9)

    def test_min_value(self):
        """check that entry below minimum is rejected, followed by acceptance of minimum"""
        with mock.patch('builtins.input', side_effect=(
                str(self.min_value - 1), str(self.min_value))):
            entry = minesweep.get_single_input(self.prompt, self.min_value, self.max_value)
        self.assertEqual(entry, self.min_value)

    def test_max_value(self):
        """check that entry above maximum is rejected, followed by acceptance of maximum"""
        with mock.patch('builtins.input', side_effect=(
                str(self.max_value + 1), str(self.max_value))):
            entry = minesweep.get_single_input(self.prompt, self.min_value, self.max_value)
        self.assertEqual(entry, self.max_value)

    def test_non_integer_input_is_rejected(self):
        """check that non-integers are rejected until we get input integer"""
        with mock.patch('builtins.input', side_effect=('a', '2.0', '3')):
            entry = minesweep.get_single_input(self.prompt, self.min_value, self.max_value)
        self.assertEqual(entry, 3)


class TestSetupMines(unittest.TestCase):
    """ test function setup_mines"""

    def setUp(self):
        self.width = 15
        self.height = 9
        self.number_of_mines = 130
        self.mines = minesweep.setup_mines(self.width, self.height, self.number_of_mines)

    def test_returned_mines_is_list(self):
        """check that mines are returned in the form of a list"""
        self.assertEqual(type(self.mines), list)

    def test_at_least_one_mine_in_form_of_tuple(self):
        """check we have at least one mine in the form of a tuple"""
        # this could be split into two tests, but that seems like overkill
        self.assertEqual(type(self.mines[0]), tuple)

    def test_mine_has_2_coordinates(self):
        """check that the tuple for the first mine has 2 coordinates"""
        # it's probably redundant to check that for all mines
        self.assertEqual(len(self.mines[0]), 2)

    def test_returned_mines_equals_number_of_mines(self):
        """check we have as many mines as intended"""
        self.assertEqual(len(self.mines), self.number_of_mines)

    def test_mine_coordinates_fit_within_width(self):
        """check that x-coordinates for each mine are less than width"""
        # note that coordinates start with 0, instead of 1
        self.assertTrue(all(mine[0] < self.width for mine in self.mines))

    def test_mine_coordinates_fit_within_height(self):
        """check that y-coordinates for each mine are less than height"""
        # note that coordinates start with 0, instead of 1
        self.assertTrue(all(mine[1] < self.height for mine in self.mines))


class TestSetupBoard(unittest.TestCase):
    """ test function setup_board"""

    def setUp(self):
        self.width = 20
        self.height = 10
        self.board = minesweep.setup_board(self.width, self.height)

    def test_returned_board_is_list(self):
        """check that board is returned in the form of a list"""
        self.assertEqual(type(self.board), list)

    def test_board_height(self):
        """check that number of items in the list, representing y coordinate, equals height"""
        self.assertEqual(len(self.board), self.height)

    def test_returned_board_has_sublists(self):
        """check that elements of the board consist of lists"""
        self.assertEqual(type(self.board[0]), list)

    def test_board_width(self):
        """check that number of items in the first sublist, representing x coordinate, equals width"""
        # note that checking for later sublists should be redundant
        self.assertEqual(len(self.board[0]), self.width)

    def test_initialisation_type(self):
        """check that board is initialised with integer values"""
        # note we should only need to check one value; assuming others cannot be different
        self.assertEqual(type(self.board[0][0]),int)

    def test_initialisation_value(self):
        """check that board is initialised with values of -1"""
        # note we should only need to check one value; assuming others cannot be different
        self.assertEqual(self.board[0][0], -1)


class TestGetMove(unittest.TestCase):
    """test function get_move"""

    """I don't know yet how to test the exit function if  q  is entered.
    As a result the call to the function is included in the setUp below.
    If we do enter  q  as a value then the call needs to be moved into the
    individual tests."""

    def setUp(self):
        # note to self: if you use side_effect instead of return_value then the mocked
        # values (even if only a single value) need to be in the form of a list
        with mock.patch('builtins.input', return_value='9 8'):
            self.move = minesweep.get_move()

    def test_return_is_tuple(self):
        """check that we get a tuple as return value"""
        self.assertEqual(type(self.move), tuple)

    def test_return_tuple_contains_two_values(self):
        """check that return tuple has two values"""
        self.assertEqual(len(self.move), 2)

    def test_return_values_are_integers(self):
        """check that return values are integers"""
        self.assertTrue(type(self.move[0]) == int and type(self.move[1]) == int)

    def test_return_values(self):
        """check that return values are entry values - 1"""
        self.assertEqual(self.move, (8,7))


class TestCountAdjacentMines(unittest.TestCase):
    """test function count_adjacent_mines
    this is going to have a lot of test cases to try"""

    def test_return_is_integer(self):
        move = (1, 1)
        mines = [(2, 2)]
        count = minesweep.count_adjacent_mines(move, mines, 3, 3)
        self.assertEqual(type(count), int)

    def test_return_is_1(self):
        move = (1, 1)
        mines = [(2, 2)]
        count = minesweep.count_adjacent_mines(move, mines, 3, 3)
        self.assertEqual(count, 1)

    def test_return_is_2(self):
        move = (1, 1)
        mines = [(2, 2), (1, 2)]
        count = minesweep.count_adjacent_mines(move, mines, 3, 3)
        self.assertEqual(count, 2)

    def test_lower_left_corner(self):
        move = (0, 0)
        mines = [(0, 1), (1, 1), (1, 0)]
        count = minesweep.count_adjacent_mines(move, mines, 3, 3)
        self.assertEqual(count, 3)

    def test_upper_left_corner(self):
        move = (0, 2)
        mines = [(0, 1), (1, 1), (1, 2)]
        count = minesweep.count_adjacent_mines(move, mines, 3, 3)
        self.assertEqual(count, 3)

    def test_upper_right_corner(self):
        move = (2, 2)
        mines = [(2, 1), (1, 1), (1, 2)]
        count = minesweep.count_adjacent_mines(move, mines, 3, 3)
        self.assertEqual(count, 3)

    def lower_right_corner(self):
        move = (2, 0)
        mines = [(2, 1), (1, 1), (1, 0)]
        count = minesweep.count_adjacent_mines(move, mines, 3, 3)
        self.assertEqual(count, 3)

    def test_return_is_4(self):
        move = (1, 1)
        mines = [(2, 2), (1, 2), (0, 0), (0, 1)]
        count = minesweep.count_adjacent_mines(move, mines, 3, 3)
        self.assertEqual(count, 4)

    def test_return_is_5(self):
        move = (1, 1)
        mines = [(2, 2), (2, 1), (1, 2), (0, 0), (0, 1)]
        count = minesweep.count_adjacent_mines(move, mines, 3, 3)
        self.assertEqual(count, 5)

    def test_return_is_6(self):
        move = (1, 1)
        mines = [(2, 2), (2, 1), (1, 2), (0, 0), (0, 1), (1, 0)]
        count = minesweep.count_adjacent_mines(move, mines, 3, 3)
        self.assertEqual(count, 6)

    def test_return_is_7(self):
        move = (1, 1)
        mines = [(2, 2), (2, 1), (1, 2), (0, 0), (0, 1), (1, 0), (2, 0)]
        count = minesweep.count_adjacent_mines(move, mines, 3, 3)
        self.assertEqual(count, 7)

    def test_return_is_8(self):
        move = (1, 1)
        mines = [(2, 2), (2, 1), (1, 2), (0, 0), (0, 1), (1, 0), (2, 0), (0, 2)]
        count = minesweep.count_adjacent_mines(move, mines, 3, 3)
        self.assertEqual(count, 8)


if __name__ == '__main__':
    unittest.main()
