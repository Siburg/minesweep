"unit tests for minesweep.py"

import minesweep
import unittest


class TestGetGameParameters(unittest.TestCase):
    """ test function get_game_paramaters"""

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

if __name__ == '__main__':
    unittest.main()
