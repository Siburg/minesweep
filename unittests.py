"""unit tests for minesweep.py"""

import minesweep
import unittest
import sys
import io


class TestGetSingleInput(unittest.TestCase):
    """ Test the helper function get_single_input that is inside the
    get_game_parameters function."""


class TestGetGameParameters(unittest.TestCase):
    """ test function get_game_parameters"""

    def test_number_of_return_values(self):
        """ check that we get 3 return values"""
        values = minesweep.get_game_parameters()
        self.assertEqual(len(values), 3)

    def test_all_return_values_are_integer(self):
        """ check that all of the return values are integer"""
        # you could split this into separate tests, but that seems like overkill
        values = minesweep.get_game_parameters()
        # did we actually need to call minesweep again? could we do it earlier?
        self.assertTrue(type(values[0]) is int
                        and type(values[1]) is int and type(values[2]) is int)

    def test_max_width_compliance(self):
        """check that returned width value remains within specified max_width"""
        max_width = 1
        values = minesweep.get_game_parameters(max_width=max_width)
        self.assertLessEqual(values[0], max_width)

    def test_max_height_compliance(self):
        """check that returned height value remains within specified max_height"""
        max_height = 1
        values = minesweep.get_game_parameters(max_height=max_height)
        self.assertLessEqual(values[1], max_height)

    def test_minimum_values(self):
        """check that all returned values are at least 1"""
        # this assumes that you also need at least 1 mine
        # this could be split into separate tests, but that seems like overkill
        values = minesweep.get_game_parameters()
        self.assertTrue(values[0] >= 1 and values[1] >= 1 and values[2] >= 1)

    def test_number_of_mines_can_fit(self):
        """check that number of mines is less than the area of the board"""
        # also allowing for at least 1 blank space; instead of having 100% mines
        values = minesweep.get_game_parameters()
        self.assertLess(values[2], values[0] * values[1])


class TestSetupGame(unittest.TestCase):
    """ test function setup_game"""

    def setUp(self):
        self.width = 20
        self.height = 10
        self.number_of_mines = 30
        self.results = minesweep.setup_game(self.width, self.height, self.number_of_mines)
        self.mines = self.results[0]
        self.board = self.results[1]

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

    def test_returned_board_is_list(self):
        """check that board is returned in the form of a list"""
        self.assertEqual(type(self.board), list)

    def test_board_width(self):
        """check that number of items in the list, representing x coordinate, equals width"""
        self.assertEqual(len(self.board), self.width)

    def test_returned_board_has_sublists(self):
        """check that elements of the board consist of lists"""
        self.assertEqual(type(self.board[0]), list)

    def test_board_height(self):
        """check that number of items in the first sublist, representing y coordinate, equals height"""
        # note that checking for later sublists should be redundant
        self.assertEqual(len(self.board[0]), self.height)


class TestDisplayBoard(unittest.TestCase):
    """ test function display_board"""
    # note this is mostly still a bunch of nonsense tests to understand print redirection
    # does not yet have anything to do with the program itself

    def setUp(self):
        self.print_redirect = io.StringIO()
        sys.stdout = self.print_redirect

    def test_something_got_printed(self):
        minesweep.display_board()
        printed = self.print_redirect.getvalue()
        # commented out statements below cause an exit failure
        # sys.stdout = sys.__stdout__
        # print_redirect.close()
        self.assertEqual(printed, 'hello\n')

    def test_same_thing_again_got_printed(self):
        print('hello again')
        printed = self.print_redirect.getvalue()
        # commented out statements below cause an exit failure
        # sys.stdout = sys.__stdout__
        # print_redirect.close()
        self.assertEqual(printed, 'hello again\n')

    def test_print_redirect_got_closed(self):
        self.assertFalse(self.print_redirect.closed)

    def test_what_happens_now(self):
        printed = self.print_redirect.readline()
        self.assertEqual(printed, "")

    def tearDown(self):
        # sys.stdout = sys.__stdout__
        self.print_redirect.__del__()
        sys.stdout = sys.__stdout__
        # io.StringIO.close()
        pass


if __name__ == '__main__':
    unittest.main()
