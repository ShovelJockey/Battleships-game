class Coordinate:

    @classmethod
    def coord_right(self, start_coord, spaces, board_size):
        new_coords = [num for num in range(start_coord[1], start_coord[1] + spaces) if num > -1 and num < board_size]
        old_coords = [start_coord[0] for val in range(spaces + 1)]
        coords = zip(old_coords, new_coords)
        coords = list(coords)
        return coords

    @classmethod
    def coord_left(self, start_coord, spaces, board_size):
        new_coords = [num for num in range(start_coord[1], start_coord[1] - spaces, -1) if num > -1 and num < board_size]
        old_coords = [start_coord[0] for val in range(spaces + 1)]
        coords = zip(old_coords, new_coords)
        coords = list(coords)
        return coords

    @classmethod
    def coord_up(self, start_coord, spaces, board_size):
        new_coords = [num for num in range(start_coord[0], start_coord[0] - spaces, -1) if num > -1 and num < board_size]
        old_coords = [start_coord[1] for val in range(spaces + 1)]
        coords = zip(new_coords, old_coords)
        coords = list(coords)
        return coords   

    @classmethod
    def coord_down(self, start_coord, spaces, board_size):
        new_coords = [num for num in range(start_coord[0], start_coord[0] + spaces) if num > -1 and num < board_size]
        old_coords = [start_coord[1] for val in range(spaces + 1)]
        coords = zip(new_coords, old_coords)
        coords = list(coords)
        return coords        

    @classmethod  
    def user_to_index(self, user_coord):
        index = int(user_coord[1:]) - 1, ord(user_coord[0]) - ord("A")
        return index

    @classmethod
    def index_to_user(self, index):
        coords = chr(index[1] + ord('A')) + str(index[0] + 1)
        return coords