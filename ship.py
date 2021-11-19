class Ships:        
    
    def __init__(self): 
        self.locations = {}
        self.hit_count = 0
        self.sunk_ships = []

    def check_all_locs(self, index):
        if any(x in index for y in self.locations.values() for x in y):
            return True
        else:
            return False

    def check_start_loc(self, index):
        for val in self.locations.values():
            if index in val:
                return True
            else:
                return False

    def place_ship(self, location_value, ship_key):
        self.locations[ship_key] = location_value
    
    def does_this_hit(self, guess):
        for val in self.locations.values():
            if guess in val:
                self.hit_count += 1         
                return True
            else:
                return False

    def has_ship_sunk(self, player_instance):
        for x in self.locations.items():
            if all(elem in player_instance.guesses for elem in x[1]):
                if x not in self.sunk_ships:
                    self.sunk_ships.append(x)
                    xsplit = (x[0]).split(' ', 1)
                    return (True, xsplit[0])
                else:
                    return False, 'none'

    #check on whether any ships have been sunk by a computer or player hit
    #needs to be able to check whether all a ships locations have been hit
    #maybe use guess list and when there is a new hit check against locations
    #need to return key for values to declare ship sunk
    #needs to be a check on which ships are sunk so they cannot be sunk by this again