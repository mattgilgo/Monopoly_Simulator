import Space

# Class for Jail space in Monopoly

class Jail(Space):

    def __init__(self, space_type="Jail"):
        super.__init__(self, space_type)
        self.jail_members = []

    def add_jail_member(self, player):
        self.jail_members.append(player)

    def remove_jail_member(self, player):
        self.jail_members.remove(player)
    
    def get_jail_members(self):
        return self.jail_members