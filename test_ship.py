import unittest
from ship import Ships
from player import HumanPlayer

class ShipsTests(unittest.TestCase):
    def setUp(self):
        self.instance = Ships()
        self.instance.locations = {'Carrier': [(0,0),(0,1),(0,2),(0,3),(0,4)]}
        self.test_Player = HumanPlayer()

    def test_check_all_locs_True(self):
        locs = [(0,0),(1,0),(2,0)]
        result = self.instance.check_all_locs(locs)
        self.assertTrue(result)

    def test_check_all_locs_False(self):
        locs = [(5,5),(5,6),(5,7)]
        result = self.instance.check_all_locs(locs)
        self.assertFalse(result)

    def test_check_start_loc_True(self):
        loc = (0,0)
        result = self.instance.check_start_loc(loc)
        self.assertTrue(result)

    def test_check_start_loc_False(self):
        loc = (2,0)
        result = self.instance.check_start_loc(loc)
        self.assertFalse(result)

    def test_place_ship(self):
        ship_key = 'battleship'
        location_value = [(7,0),(7,1),(7,2),(7,3)]
        self.instance.place_ship(location_value, ship_key)
        assert self.instance.locations[ship_key] == [(7,0),(7,1),(7,2),(7,3)]

    def test_does_this_hit_True(self):
        guess = (0,4)
        result = self.instance.does_this_hit(guess)
        self.assertTrue(result)
        assert self.instance.hit_count == 1

    def test_does_this_hit_False(self):
        guess = (9,9)
        result = self.instance.does_this_hit(guess)
        self.assertFalse(result)
        assert self.instance.hit_count == 0

    def test_has_ship_sunk(self):
        self.test_Player.guesses = [(0,0),(0,4),(0,3),(0,2),(0,1)]
        result = self.instance.has_ship_sunk(self.test_Player)
        expected = ('Carrier', [(0,0),(0,1),(0,2),(0,3),(0,4)])
        assert result == expected

unittest.main()