import Utility

# Class representing a Property in Monopoly

class Property(Utility):

    def __init__(self, title, purchase_value, rent, mortgage_value, home_cost, color):
        super.__init__(self, title, purchase_value, mortgage_value, color)
        self.owner = ""
        self.rent = rent
        self.home_cost = home_cost
        self.num_homes = 0
    
    def set_owner(self, player):
        self.owner = player
    
    def add_homes(self, num_homes_added):
        if self.get_num_homes() + num_homes_added <= 5:
            self.num_homes = self.get_num_homes() + num_homes_added
        else:
            print("You cannot have more than 5 homes! Please add an appropriate number of houses")
    
    def get_owner(self):
        return self.owner
    
    def get_num_homes(self):
        return self.num_homes
    