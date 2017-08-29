"""unit tests for minesweep.py"""

import minesweep
import unittest
#from unittest import mock
#import sys
#import io


class TestSetupMines(unittest.TestCase):
    """ test function setup_mines"""

    def setUp(self):
        self.width = 20
        self.height = 10
        self.number_of_mines = 30
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


if __name__ == '__main__':
    unittest.main()
