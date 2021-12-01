from coordinate import Coordinate


class HumanPlayer:

    def __init__(self):
        self.guesses = []

    def player_introduction(self):
        print('''
        How to play:\n
        This battleships game works on a 10x10 board, rows are numbered 1-10 and columns are lettered A-J.\n
        You will see your board with your ships and the computers guesses, you will also see the computer board with your guesses both hits and misses.\n
        To play first you need to place your ships, then take turns with the computer guessing where each others ships are until either you sink all its ships or it sinks all of yours.\n
        On your board ship locations will be represented by a letter in each coordinate (C for Carrier, B for Battleship, D for Destroyer and S for Submarine).\n
        For both the computer and player guesses that are hits will be represented with an 'X' and misses with an 'O'.
        ''')
        input('\nPress enter when you are ready to continue ')

    def ship_input_introduction(self):
        print('''
        You need to assign coordinates to each of your 4 ship types, to do this first enter a starting coordinate then an alignment.\n
        For example a 4 space ship at coordinate 'A5 right', would be placed at A5, B5, C5 and D5.\n
        Below is the different ship type lengths and amounts:
        ship type - size - amount
        Carrier   -  5   -   1
        Battleship-  4   -   2
        Destroyer -  3   -   2
        Submarine -  2   -   3
        ''')
        input('\nPress enter when you are ready to continue ')

    def format_input(self, coord):
        coord = coord.replace(' ', '')
        coord = coord.upper()
        try:
            if coord[0].isalpha() and coord[1:].isdecimal():
                index = Coordinate.user_to_index(coord)
                return index
            else:
                print('Sorry that is not a valid coordinate, it must be a letter from A-J and a number from 1-10, eg A1')
        except IndexError:
            print('Sorry that is not a valid coordinate, it must be a letter from A-J and a number from 1-10, eg A1')

    def ship_orientation(self, format_coord, orientation, ship_type, ship_size, player_ship_instance, player_board, ship_number, ship_letter, dict_name):
        ship_location = orientation(format_coord, ship_size, 10)
        if player_ship_instance.check_all_locs(ship_location) or len(ship_location) != ship_size: 
            print('Sorry either one of these coordinates has been taken or one of these coordinates does not exist on the board')
            new_start_coor_option = input('Enter 1 if you would like to try a different orientation or 2 if you would like to change your starting coordinate   ')
            if new_start_coor_option == '1':
                return True
            else:
                self.ship_input(ship_type, ship_size, player_ship_instance, player_board, ship_number, ship_letter, dict_name)
        else:
            player_ship_instance.place_ship(ship_location, dict_name)
            print(player_ship_instance.locations.items())
            player_board.player_set_ship(ship_location, ship_letter)
            return False
        
    def ship_input(self, ship_type, ship_size, player_ship_instance, player_board, ship_number, ship_letter, dict_name):
        coord = input(f'Enter a coordinate for your{ship_number} {ship_type}   ')
        format_coord = self.format_input(coord)
        if format_coord == None:
            print('Sorry thats not a valid coordinate')
            self.ship_input(ship_type, ship_size, player_ship_instance, player_board, ship_number, ship_letter, dict_name)
        if player_ship_instance.check_start_loc(format_coord):
            print('Sorry this coordinate is already occupied!')
            self.ship_input(ship_type, ship_size, player_ship_instance, player_board, ship_number, ship_letter, dict_name)                              
        not_placed = True
        while not_placed == True:                                     
            orientation = input('''From your coordinate what orientation would you like to place your ship on?\nenter 'up', 'down', 'left' or 'right':   ''')
            if orientation.lower() == 'up':
                not_placed = self.ship_orientation(format_coord, Coordinate.coords_up, ship_type, ship_size, player_ship_instance, player_board, ship_number, ship_letter, dict_name)
            elif orientation.lower() == 'down':
                not_placed = self.ship_orientation(format_coord, Coordinate.coords_down, ship_type, ship_size, player_ship_instance, player_board, ship_number, ship_letter, dict_name)       
            elif orientation.lower() == 'left':
                not_placed = self.ship_orientation(format_coord, Coordinate.coords_left, ship_type, ship_size, player_ship_instance, player_board, ship_number, ship_letter, dict_name)
            elif orientation.lower() == 'right':
                not_placed = self.ship_orientation(format_coord, Coordinate.coords_right, ship_type, ship_size, player_ship_instance, player_board, ship_number, ship_letter, dict_name)

    def player_guess(self, computer_ship_instance, computer_board_instance, player_instance):
        player_guess = input('enter a coordinate to shoot at   ')
        format_guess = self.format_input(player_guess)
        if format_guess == None:
            self.player_guess(computer_ship_instance, computer_board_instance, player_instance)
        if format_guess in self.guesses:
            print('Sorry you have already guessed this coordinate')
            self.player_guess(computer_ship_instance, computer_board_instance, player_instance)
        self.guesses.append(format_guess)
        if computer_ship_instance.does_this_hit(format_guess):
            print('you hit!')
            computer_board_instance.update_board(format_guess, 'X')
            sunk_ship = computer_ship_instance.has_ship_sunk(player_instance)
            if sunk_ship:
                sunk_ship = (sunk_ship[0]).split(' ', 1)
                print(f'You have sunk an enemy {sunk_ship}!')
        else:
            print('you missed!')
            computer_board_instance.update_board(format_guess, 'O')