import random
from coordinate import Coordinate


class Computer_Player:

    def __init__(self):
        self.guesses = []
        self.adjacent_coords = []
        self.has_hit = False
        self.checking_adjacent = False
        self.adjacent_hit = False
        self.last_rand_guess_loc = None
        self.adjacent_hit_loc = None
    
    def create_computer_ships(self, ship_size, computer_ship_instance, dict_name):
        ship_start_loc = (random.randint(0, 9), random.randint(0, 9))
        orientation = random.randint(1, 4)
        if orientation == 1:
            ship_location = Coordinate.coords_up(ship_start_loc, ship_size, 10)
            if computer_ship_instance.check_all_locs(ship_location) or len(ship_location) != ship_size:
                self.create_computer_ships(ship_size, computer_ship_instance, dict_name)
            else:
                computer_ship_instance.place_ship(ship_location, dict_name)
        elif orientation == 2:
            ship_location = Coordinate.coords_down(ship_start_loc, ship_size, 10)
            if computer_ship_instance.check_all_locs(ship_location) or len(ship_location) != ship_size:
                self.create_computer_ships(ship_size, computer_ship_instance, dict_name)
            else:
                computer_ship_instance.place_ship(ship_location, dict_name)
        elif orientation == 3:
            ship_location = Coordinate.coords_right(ship_start_loc, ship_size, 10)
            if computer_ship_instance.check_all_locs(ship_location) or len(ship_location) != ship_size:
                self.create_computer_ships(ship_size, computer_ship_instance, dict_name)
            else:
                computer_ship_instance.place_ship(ship_location, dict_name)
        elif orientation == 4:
            ship_location = Coordinate.coords_left(ship_start_loc, ship_size, 10)
            if computer_ship_instance.check_all_locs(ship_location) or len(ship_location) != ship_size:
                self.create_computer_ships(ship_size, computer_ship_instance, dict_name)
            else:
                computer_ship_instance.place_ship(ship_location, dict_name)

    def computer_guess(self, player_ship_instance, player_board_instance, computer_instance):
        if not self.has_hit:  #make into function? This is the default       
            comp_guess = (random.randint(0, 9), random.randint(0, 9))
            if comp_guess in self.guesses:
                self.computer_guess(player_ship_instance, player_board_instance, computer_instance)
            else:
                self.guesses.append(comp_guess)
                output_guess = Coordinate.index_to_user(comp_guess)
                if player_ship_instance.does_this_hit(comp_guess):
                    self.last_rand_guess_loc = comp_guess
                    print(f'The computer has hit your ship at {output_guess}')
                    player_board_instance.update_board(comp_guess, 'X')
                    sunk = player_ship_instance.has_ship_sunk(computer_instance)
                    if sunk:
                        print(f'The computer sunk your {player_ship_instance.sunk_ship_names[-1]}!')
                    else:
                        self.has_hit = True          
                else:
                    print(f'The computer missed your ships shooting at {output_guess}')
                    player_board_instance.update_board(comp_guess, 'O')
                    self.has_hit = False
        elif self.has_hit: #make into function? Just after making random hit
            if not self.checking_adjacent:
                if not self.adjacent_hit:
                    self.adjacent_coords = Coordinate.all_adjacent(self.last_rand_guess_loc, 10)#make possible adjacent coords on board
                    avaliable_adjacent_coords = [x for x in self.adjacent_coords if x not in self.guesses]#filter out guessed adjacent
                    comp_guess = random.choice(avaliable_adjacent_coords)
                    self.guesses.append(comp_guess)
                    output_guess = Coordinate.index_to_user(comp_guess)
                    if player_ship_instance.does_this_hit(comp_guess):#check if rand guess from adjacent coords hits
                        print(f'The computer has hit your ship at {output_guess}')
                        player_board_instance.update_board(comp_guess, 'X')
                        sunk = player_ship_instance.has_ship_sunk(computer_instance)
                        if sunk:  #if it sinks it resets has_hit back to making random guesses
                            print(f'The computer sunk your {player_ship_instance.sunk_ship_names[-1]}!')
                            self.has_hit = False
                        else:
                            self.adjacent_hit_loc = comp_guess
                            self.adjacent_hit = True
                    else:
                        print(f'The computer missed your ships shooting at {output_guess}')
                        player_board_instance.update_board(comp_guess, 'O')
                        self.checking_adjacent = True
                elif self.adjacent_hit:
                    orientation = Coordinate.find_orientation(self.last_rand_guess_loc, self.adjacent_hit_loc)
                    coords1 = Coordinate.dir_adjacent(orientation, self.last_rand_guess_loc, 10)
                    coords2 = Coordinate.dir_adjacent(orientation, self.adjacent_hit_loc, 10)
                    adj_coords = [x for x in coords1 + coords2 if x not in self.guesses]
                    if adj_coords:
                        comp_guess= random.choice(adj_coords)
                        self.guesses.append(comp_guess)
                        output_guess = Coordinate.index_to_user(comp_guess)
                        if player_ship_instance.does_this_hit(comp_guess):#check if rand guess from adjacent coords hits
                            print(f'The computer has hit your ship at {output_guess}')
                            player_board_instance.update_board(comp_guess, 'X')
                            sunk = player_ship_instance.has_ship_sunk(computer_instance)
                            if sunk:  #if it sinks it resets has_hit back to making random guesses
                                print(f'The computer sunk your {player_ship_instance.sunk_ship_names[-1]}!')
                                self.has_hit = False
                                self.adjacent_hit = False
                            else:
                                self.adjacent_hit_loc = comp_guess
                        else:
                            print(f'The computer missed your ships shooting at {output_guess}')
                            player_board_instance.update_board(comp_guess, 'O')
            elif self.checking_adjacent: #make into function?
                avaliable_adjacent_coords = [x for x in self.adjacent_coords if x not in self.guesses]
                if avaliable_adjacent_coords:
                    comp_guess = random.choice(avaliable_adjacent_coords)
                    self.guesses.append(comp_guess)
                    output_guess = Coordinate.index_to_user(comp_guess)
                    if player_ship_instance.does_this_hit(comp_guess):
                        print(f'The computer has hit your ship at {output_guess}')
                        player_board_instance.update_board(comp_guess, 'X')
                        sunk = player_ship_instance.has_ship_sunk(computer_instance)
                        if sunk:
                            print(f'The computer sunk your {player_ship_instance.sunk_ship_names[-1]}!')
                            self.has_hit = False
                            self.checking_adjacent = False
                        else:
                            self.adjacent_hit = True
                            self.checking_adjacent = False
                    else:
                        print(f'The computer missed your ships shooting at {output_guess}')
                        player_board_instance.update_board(comp_guess, 'O')
                else:
                    self.has_hit = False
                    self.checking_adjacent = False
                    self.computer_guess(player_ship_instance, player_board_instance, computer_instance)