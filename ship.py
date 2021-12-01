class Ships:        
    
    def __init__(self): 
        self.locations = {}
        self.hit_count = 0
        self.sunk_ships = []

    def check_all_locs(self, locs):
        return any(x in locs for y in self.locations.values() for x in y)

    def check_start_loc(self, index):
        if any(x for x in self.locations.values() if index in x):
            return True

    def place_ship(self, location_value, ship_key):
        self.locations[ship_key] = location_value
    
    def does_this_hit(self, guess):
        if any(x for x in self.locations.values() if guess in x):
                self.hit_count += 1         
                return True

    def has_ship_sunk(self, other_player_instance):
        for x in self.locations.items():
            if all(elem in other_player_instance.guesses for elem in x[1]):
                if x not in self.sunk_ships:
                    self.sunk_ships.append(x)
                    return x