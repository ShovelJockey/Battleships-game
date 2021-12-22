import unittest
from game import Game

class PlayerTests(unittest.TestCase):
    def setUp(self):
        self.instance = Game()

    def test_computer_set_ships(self):#comment out Human player ship input for test
        self.instance.game_set_ships()
        ship_locations = 25
        list_of_locs = self.instance.computer_ships.locations.values()
        unique_test = [item for sublist in list_of_locs for item in sublist]
        unique_test = set(unique_test)
        assert len(unique_test) == ship_locations

unittest.main()