class Ships:        
    
    def __init__(self): 
        self.locations = []
        self.hit_count = 0

    def check_all_locs(self, index):
        if any(x in index for x in self.locations):
            return True
        else:
            return False

    def check_start_loc(self, index):
        if index in self.locations:
            return True
        else:
            return False

    def place_ship(self, location):
        self.locations += location
    
    def does_this_hit(self, guess):
        if guess in self.locations:
            self.hit_count += 1
            return True
        else:
            return False