import unittest
from player import HumanPlayer

class PlayerTests(unittest.TestCase):
    def setUp(self):
        self.player = HumanPlayer()
        self.player.guesses = [(0,0)]

    def test_format(self):
        input = 'A 1'
        board_size = 10
        expected = (0,0)
        actual = self.player.format_input(input, board_size)
        assert expected == actual

    def test_format_out_of_ranges(self):
        input = 'A11'
        board_size = 10
        result = self.player.format_input(input, board_size)
        self.assertIsNone(result)

unittest.main()