"unit tests for minesweep.py"

import minesweep
import unittest
import sys
import io


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
        self.assertTrue(values[0] >= 1 and values[1] >=1 and values[2] >= 1)

    def test_number_of_mines_can_fit(self):
        """check that number of mines is less than the area of the board"""
        # also allowing for at least 1 blank space; instead of having 100% mines
        values = minesweep.get_game_parameters()
        self.assertLess(values[2], values[0] * values[1])


class TestSetupGame(unittest.TestCase):
    """ test function setup_game"""
    pass


class TestDisplayBoard(unittest.TestCase):
    """ test function display_board"""

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
        minesweep.display_board()
        printed = self.print_redirect.getvalue()
        # commented out statements below cause an exit failure
        # sys.stdout = sys.__stdout__
        # print_redirect.close()
        self.assertEqual(printed, 'hello\n')

    def tearDown(self):
        # sys.stdout = sys.__stdout__
        # self.print_redirect.close()
        pass



if __name__ == '__main__':
    unittest.main()
