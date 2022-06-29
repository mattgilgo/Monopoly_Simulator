import Utility

# Class representing a Property in Monopoly

class Property(Utility):

    def __init__(self, title, purchase_value, rent, mortgage_value, home_cost, color):
        super.__init__(self, title, purchase_value, mortgage_value, color)
        self.owner = ""
        self.original_rent = rent
        self.rent = rent
        self.home_cost = home_cost
        self.num_homes = 0
    
    def set_owner(self, player):
        self.owner = player
    
    def add_homes(self, num_homes_added):
        if self.get_num_homes() + num_homes_added <= 5:
            self.num_homes = self.get_num_homes() + num_homes_added
            self.set_rent()
        else:
            print("You cannot have more than 5 homes! Please add an appropriate number of houses")
    
    def set_rent(self):
        if self.group == "Purple":
            if self.get_num_homes() == 0:
                self.rent = self.original_rent
            elif self.get_num_homes() == 1:
                self.rent = self.original_rent * 5
            elif self.get_num_homes() == 2:
                self.rent = self.original_rent * 15
            elif self.get_num_homes() == 3:
                self.rent = self.original_rent * 45
            elif self.get_num_homes() == 4:
                self.rent = self.original_rent * 80
            else:
                self.rent = self.original_rent * 125
        elif self.group == "Blue":
            if self.get_num_homes() == 0:
                self.rent = self.original_rent
            elif self.get_num_homes() == 1:
                self.rent = self.original_rent * 5
            elif self.get_num_homes() == 2:
                self.rent = self.original_rent * 15
            elif self.get_num_homes() == 3:
                self.rent = self.original_rent * 45
            elif self.get_num_homes() == 4:
                self.rent = self.original_rent * 80
            else:
                self.rent = self.original_rent * 125
                        
    
    def get_owner(self):
        return self.owner
    
    def get_num_homes(self):
        return self.num_homes

    def get_rent(self):
        return self.rent

    def get_group(self):
        return self.group



    
    