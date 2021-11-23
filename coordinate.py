class Coordinate:

    @classmethod
    def coords_right(cls, start_coord, spaces, board_size):
        new_coords = [num for num in range(start_coord[1], start_coord[1] + spaces) if num > -1 and num < board_size]
        old_coords = [start_coord[0] for val in range(spaces + 1)]
        coords = zip(old_coords, new_coords)
        coords = list(coords)
        return coords

    @classmethod
    def coords_left(cls, start_coord, spaces, board_size):
        new_coords = [num for num in range(start_coord[1], start_coord[1] - spaces, -1) if num > -1 and num < board_size]
        old_coords = [start_coord[0] for val in range(spaces + 1)]
        coords = zip(old_coords, new_coords)
        coords = list(coords)
        return coords

    @classmethod
    def coords_up(cls, start_coord, spaces, board_size):
        new_coords = [num for num in range(start_coord[0], start_coord[0] - spaces, -1) if num > -1 and num < board_size]
        old_coords = [start_coord[1] for val in range(spaces + 1)]
        coords = zip(new_coords, old_coords)
        coords = list(coords)
        return coords   

    @classmethod
    def coords_down(cls, start_coord, spaces, board_size):
        new_coords = [num for num in range(start_coord[0], start_coord[0] + spaces) if num > -1 and num < board_size]
        old_coords = [start_coord[1] for val in range(spaces + 1)]
        coords = zip(new_coords, old_coords)
        coords = list(coords)
        return coords        

    @classmethod  
    def user_to_index(cls, user_coord):
        index = int(user_coord[1:]) - 1, ord(user_coord[0]) - ord("A")
        return index

    @classmethod
    def index_to_user(cls, index):
        coords = chr(index[1] + ord('A')) + str(index[0] + 1)
        return coords

    @classmethod
    def all_adjacent(cls, coord, board_size):
        adjacent_coords = []
        up = (coord[0]-1, coord[1])
        if up[0] < board_size and up[0] > -1:
            adjacent_coords.append(up)
        down = (coord[0]+1, coord[1])
        if down[0] < board_size and down[0] > -1:
            adjacent_coords.append(down)
        right = (coord[0], coord[1]+1)
        if right[1] < board_size and right[1] > -1:
            adjacent_coords.append(right)
        left = (coord[0], coord[1]-1)
        if left[1] < board_size and left[1] > -1:
            adjacent_coords.append(left)
        return adjacent_coords

    @classmethod
    def dir_adjacent(cls, direction, coord, board_size):
        if direction == 'horizontal':
            horizontal_coords = []
            right_coord = (coord[0], coord[1]+1)
            if right_coord[1] < board_size and right_coord[1] > -1:
                horizontal_coords.append(right_coord)
            left_coord = (coord[0], coord[1]-1)
            if left_coord[1] < board_size and left_coord[1] > -1:
                horizontal_coords.append(left_coord)
            return horizontal_coords
        elif direction == 'vertical':
            vertical_coords = []
            up_coord = (coord[0]-1, coord[1])
            if up_coord[0] < board_size and up_coord[0] > -1:
                vertical_coords.append(up_coord)
            down_coord = (coord[0]+1, coord[1])
            if down_coord[0] < board_size and down_coord[0] > -1:
                vertical_coords.append(down_coord)
            return vertical_coords

    @classmethod
    def find_orientation(cls, coord, coord2):
        if coord[0] == coord2[0] and coord[1] != coord2[1]:
            return 'horizontal'
        elif coord[1] == coord2[1] and coord[0] != coord2[0]:
            return 'vertical'
        else:
            print('not on same row or column')