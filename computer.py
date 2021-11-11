import random
from coordinate import Coordinate


class Computer_Player:

    def __init__(self):
        self.guesses = []
        self.last_guess_hit = False
    
    def create_computer_ships(self, ship_size, computer_ship_instance):
        ship_start_loc = (random.randint(0, 9), random.randint(0, 9))
        orientation = random.randint(1, 4)
        if orientation == 1:
            ship_location = Coordinate.coord_up(ship_start_loc, ship_size, 10)
            if computer_ship_instance.check_all_locs(ship_location) or len(ship_location) != ship_size:
                self.create_computer_ships(ship_size, computer_ship_instance)
            else:
                computer_ship_instance.place_ship(ship_location)
        elif orientation == 2:
            ship_location = Coordinate.coord_down(ship_start_loc, ship_size, 10)
            if computer_ship_instance.check_all_locs(ship_location) or len(ship_location) != ship_size:
                self.create_computer_ships(ship_size, computer_ship_instance)
            else:
                computer_ship_instance.place_ship(ship_location)
        elif orientation == 3:
            ship_location = Coordinate.coord_right(ship_start_loc, ship_size, 10)
            if computer_ship_instance.check_all_locs(ship_location) or len(ship_location) != ship_size:
                self.create_computer_ships(ship_size, computer_ship_instance)
            else:
                computer_ship_instance.place_ship(ship_location)
        elif orientation == 4:
            ship_location = Coordinate.coord_left(ship_start_loc, ship_size, 10)
            if computer_ship_instance.check_all_locs(ship_location) or len(ship_location) != ship_size:
                self.create_computer_ships(ship_size, computer_ship_instance)
            else:
                computer_ship_instance.place_ship(ship_location)

    def computer_guess(self, player_ship_instance, player_board_instance):
        comp_guess = (random.randint(0, 9), random.randint(0, 9))
        if comp_guess in self.guesses:
            self.computer_guess(player_ship_instance, player_board_instance)
        else:
            self.guesses.append(comp_guess)
            output_guess = Coordinate.index_to_user(comp_guess)
            if player_ship_instance.does_this_hit(comp_guess):
                print(f'The computer has hit your ship at {output_guess}')
                player_board_instance.update_board(comp_guess, 'X')
            else:
                print(f'The computer missed your ships shooting at {output_guess}')
                player_board_instance.update_board(comp_guess, 'O')

