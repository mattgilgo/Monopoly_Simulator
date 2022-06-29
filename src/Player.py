# Player in a monopoly game and all their attributes

class Player(object):

    def __init__(self, name, game_piece, money=1500):
        self.set_name(name)
        self.set_game_piece(game_piece)
        self.set_money(money)
        self.properties = []
        self.get_out_of_jail_free = False

    def set_name(self, name):
        self.name = name
    
    def set_game_piece(self, game_piece):
        self.game_piece = game_piece
    
    def set_money(self, money):
        self.money = money

    def add_property(self, property):
        self.properties.append(property)

    def get_name(self):
        return self.name

    def get_game_piece(self):
        return self.game_piece
    
    def get_money(self):
        return self.money

    def get_properties(self):
        return self.properties
