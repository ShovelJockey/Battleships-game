from board import Board
from computer import Computer_Player
from coordinate import Coordinate
from player import Human_Player
from ship import Ships


class Game:

    def __init__(self):
        self.player = Human_Player()
        self.computer = Computer_Player()
        self.player_board = Board(10, 'Player Board')
        self.computer_board = Board(10, 'Computer Board')
        self.player_ships = Ships()
        self.computer_ships = Ships()

    def game_intro(self):
        self.player.player_introduction()
        self.player.ship_input_introduction()

    def game_set_ships(self):
        self.player.ship_input('Carrier', 5, self.player_ships, self.player_board, 'only', 'C')
        self.player.ship_input('Battleship', 4, self.player_ships, self.player_board, 'first', 'B')
        self.player.ship_input('Battleship', 4, self.player_ships, self.player_board, 'second', 'B')
        self.player.ship_input('Destroyer', 3, self.player_ships, self.player_board, 'first', 'D')
        self.player.ship_input('Destroyer', 3, self.player_ships, self.player_board, 'second', 'D')
        self.player.ship_input('Submarine', 2, self.player_ships, self.player_board, 'first', 'S')
        self.player.ship_input('Submarine', 2, self.player_ships, self.player_board, 'second', 'S')
        self.player.ship_input('Submarine', 2, self.player_ships, self.player_board, 'third', 'S')
        self.computer.create_computer_ships(5, self.computer_ships)
        self.computer.create_computer_ships(4, self.computer_ships)
        self.computer.create_computer_ships(4, self.computer_ships)
        self.computer.create_computer_ships(3, self.computer_ships)
        self.computer.create_computer_ships(3, self.computer_ships)
        self.computer.create_computer_ships(2, self.computer_ships)
        self.computer.create_computer_ships(2, self.computer_ships)
        self.computer.create_computer_ships(2, self.computer_ships)

    def game_running(self):
        while True:
            self.player.player_guess(self.computer_ships, self.computer_board)
            if self.computer_ships.hit_count >= 25:
                print('you have destroyed all the enemy ships, you win!')
                break
            else:
                self.computer.computer_guess(self.player_ships, self.player_board)
                if self.player_ships.hit_count >= 25:
                    print('The computer has destroyed all your ships, you lose!')
                    break
                else:
                    pass

    def game_start(self):
        self.game_intro()
        self.game_set_ships()
        self.game_running()

if __name__ == '__main__':
    game = Game()
    game.game_start()