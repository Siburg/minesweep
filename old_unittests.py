"""unit tests for minesweep.py"""

import minesweep
import unittest
from unittest import mock
import sys
import io


@unittest.skip('I/O redirection not working anymore')
class TestGetGameParameters(unittest.TestCase):
    """ test function get_game_parameters"""

    def setUp(self):
        self.print_redirect = io.StringIO()
        sys.stdout = self.print_redirect

    def tearDown(self):
        self.print_redirect.__del__()
        sys.stdout = sys.__stdout__


@unittest.skip('No tests for display_board yet')
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
