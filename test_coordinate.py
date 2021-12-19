import unittest
from coordinate import Coordinate

class CoordinateTests(unittest.TestCase):
    def setUp(self):
        self.spaces = 5
        self.spaces1 = 3
        self.board = 10

    def test_coords_right(self):
        expected = [(0,0), (0,1), (0,2), (0,3), (0,4)]
        actual = Coordinate.coords_right((0,0), self.spaces, self.board)
        assert expected == actual

    def test_coords_left(self):
        expected = [(0,0)]
        actual = Coordinate.coords_left((0,0), self.spaces1, self.board)
        assert expected == actual

    def test_coords_up(self):
        expected = [(0,0)]
        actual = Coordinate.coords_up((0,0), self.spaces, self.board)
        assert expected == actual

    def test_coords_down(self):
        expected = [(0,0), (1,0), (2,0)]
        actual = Coordinate.coords_down((0,0), self.spaces1, self.board)
        assert expected == actual
        
    def test_user_to_index(self):
        user_coord = 'A10'
        expected = (9,0)
        actual = Coordinate.user_to_index(user_coord)
        assert expected == actual

    def test_index_to_user(self):
        expected = ('F6')
        actual = Coordinate.index_to_user((5,5))
        assert expected == actual

    def test_all_adjacent(self):
        expected = [(6,7), (8,7), (7,8), (7,6)]
        actual = Coordinate.all_adjacent((7,7), self.board)
        assert expected == actual

    def test_dir_adjacent(self):
        expected = [(1,2), (1,0)]
        actual = Coordinate.dir_adjacent('horizontal', (1,1), self.board)
        assert expected == actual

    def test_find_orientation(self):
        coord1 = (4, 4)
        coord2 = (4, 5)
        expected = 'horizontal'
        actual = Coordinate.find_orientation(coord1, coord2)
        assert expected == actual

unittest.main()