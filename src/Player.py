# Player in a monopoly game and all their attributes

class Player(object):

    def __init__(self, name, game_piece, money=1500):
        self.set_name(name)
        self.set_game_piece(game_piece)
        self.money = money
        self.properties = []
        self.railroads = []
        self.utilities = []
        self.location = 0
        self.get_out_of_jail_free = False

    def set_name(self, name):
        self.name = name
    
    def set_game_piece(self, game_piece):
        self.game_piece = game_piece
    
    def set_money(self, money):
        self.money = money

    def add_property(self, property):
        self.properties.append(property)
        remaining_money = self.money - property.purchase_value
        self.money = remaining_money
    
    def add_railroad(self, railroad):
        self.railroads.append(railroad)
        remaining_money = self.money - railroad.purchase_value
        self.money = remaining_money
    
    def add_utility(self, utility):
        self.utilities.append(utility)
        remaining_money = self.money - utility.purchase_value
        self.money = remaining_money    

    def get_name(self):
        return self.name

    def get_game_piece(self):
        return self.game_piece
    
    def get_money(self):
        return self.money

    def get_properties(self):
        return self.properties
    
    def get_data(self):
        player_data = [self.name, self.game_piece, self.properties, self.money]
        return player_data

    def move_player(self, num_spaces):
        if self.location + num_spaces < 40:
            self.location = self.location + num_spaces
        else:
            self.location = self.location + num_spaces - 40
