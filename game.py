from board import Board
from computer import ComputerPlayer
from coordinate import Coordinate
from player import HumanPlayer
from ship import Ships
import time


class Game:

    def __init__(self):
        self.player = HumanPlayer()
        self.computer = ComputerPlayer()
        self.player_board = Board(10, 'Player Board')
        self.computer_board = Board(10, 'Computer Board')
        self.player_ships = Ships()
        self.computer_ships = Ships()

    def game_intro(self):
        self.player.player_introduction()
        self.player.ship_input_introduction()

    def game_set_ships(self):
        print(self.player_board)
        self.player.ship_input('Carrier', 5, self.player_ships, self.player_board, '', 'C', 'Carrier')
        self.player.ship_input('Battleship', 4, self.player_ships, self.player_board, ' first', 'B', 'Battleship 1')
        self.player.ship_input('Battleship', 4, self.player_ships, self.player_board, ' second', 'B', 'Battleship 2')
        self.player.ship_input('Destroyer', 3, self.player_ships, self.player_board, ' first', 'D', 'Destroyer 1')
        self.player.ship_input('Destroyer', 3, self.player_ships, self.player_board, ' second', 'D', 'Destroyer 2')
        self.player.ship_input('Submarine', 2, self.player_ships, self.player_board, ' first', 'S', 'Submarine 1')
        self.player.ship_input('Submarine', 2, self.player_ships, self.player_board, ' second', 'S', 'Submarine 2')
        self.player.ship_input('Submarine', 2, self.player_ships, self.player_board, ' third', 'S', 'Submarine 3')
        self.computer.create_computer_ships(5, self.computer_ships, 'Carrier')
        self.computer.create_computer_ships(4, self.computer_ships, 'Battleship 1')
        self.computer.create_computer_ships(4, self.computer_ships, 'Battleship 2')
        self.computer.create_computer_ships(3, self.computer_ships, 'Destroyer 1')
        self.computer.create_computer_ships(3, self.computer_ships, 'Destroyer 2')
        self.computer.create_computer_ships(2, self.computer_ships, 'Submarine 1')
        self.computer.create_computer_ships(2, self.computer_ships, 'Submarine 2')
        self.computer.create_computer_ships(2, self.computer_ships, 'Submarine 3')

    def game_running(self):
        while True:
            self.player.player_guess(self.computer_ships, self.computer_board, self.player)
            if self.computer_ships.hit_count >= 25:
                print('you have destroyed all the enemy ships, you win!')
                break
            else:
                input('Press enter to end your turn ')
                self.computer.computer_guess(self.player_ships, self.player_board, self.computer)
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