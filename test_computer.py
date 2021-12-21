import unittest
from computer import ComputerPlayer
from ship import Ships
from board import Board

class PlayerTests(unittest.TestCase):
    def setUp(self):
        self.instance = ComputerPlayer()
        self.test_Ships = Ships()
        self.test_board = Board(10, 'test')

    def test_create_computer_ships(self):
        ship_size = 5
        self.instance.create_computer_ships(ship_size, self.test_Ships, 'carrier')
        assert len(self.test_Ships.locations['carrier']) == ship_size

    def test_create_computer_ships_dif_loc(self):
        ship_size = 5
        self.instance.create_computer_ships(ship_size, self.test_Ships, 'carrier')
        self.instance.create_computer_ships(ship_size, self.test_Ships, 'carrier1')
        assert any(self.test_Ships.locations['carrier']) not in self.test_Ships.locations['carrier1']

    def test_computer_guess(self):
        self.instance.computer_guess(self.test_Ships, self.test_board, self.instance)

    def test_computer_guess_has_hit(self):
        self.instance.has_hit = True
        self.instance.last_rand_guess_loc = (0,0)
        self.instance.computer_guess(self.test_Ships, self.test_board, self.instance)

unittest.main()