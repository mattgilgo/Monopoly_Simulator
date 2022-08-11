# Class representing space on game board

from tokenize import group


class Space(object):

    def __init__(self, title, space_type, purchase_value, rent, rent_1home, rent_2homes, rent_3homes, rent_4homes, rent_hotel, house_cost, mortgage_value, group_color):
        self.title = title
        self.space_type = space_type
        self.purchase_value = purchase_value
        self.rent = rent
        self.rent_1home = rent_1home
        self.rent_2homes = rent_2homes
        self.rent_3homes = rent_3homes
        self.rent_4homes = rent_4homes
        self.rent_hotel = rent_hotel
        self.house_cost = house_cost
        self.mortgage_value = mortgage_value
        self.group_color = group_color
        self.owned = False
        self.owner = ""

    def set_space_type(self, space_type):
        self.space_type = space_type

    def get_space_type(self):
        return self.space_type