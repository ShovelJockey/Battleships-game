class Board:
    def __init__(self, size, name):
        self.game_board = [[None for row in range(size)] for row in range(size)]
        self.name = name

    def player_set_ship(self, ship_loc, ship_marker):
        for x,y in ship_loc:
            self.game_board[x][y] = ship_marker
        print(self)

    def computer_set_ship(self, ship_loc, ship_marker):
        for x,y in ship_loc:
            self.game_board[x][y] = ship_marker

    def update_board(self, index, marker):
        x, y = index
        self.game_board[x][y] = marker
        print(self)

    def __str__(self):
        return (
            ''.join(f'{self.name}\n')
            + ''.join('   ')
            + ' '.join(chr(ord('A') + col) for col in range(len(self.game_board)))
            + ''.join('\n')
            + '\n'.join(str(num + 1).ljust(3)
            + ' '.join(val if val else ' ' for val in row) for num, row in enumerate(self.game_board))
            )
