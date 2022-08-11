import Board
import Property
import Utility
import Space
import pandas as pd

# Class for a Monopoly Board

class MonopolyBoard(Board):
    
    def __init__(self):
        spaces = MonopolyBoard.generate_monopoly_spaces()
        super.__init__(spaces)
        self.free_parking = 0


    def generate_monopoly_spaces():
        spaces_df = pd.read_csv('monopoly_spaces.csv')
        spaces = [(Space(row.Title, row.SpaceType, row.PurchaseValue, row.Rent, row.Rent1Home, row.Rent2Homes, row.Rent3Homes, row.Rent4Homes, row.RentHotel, row.HouseCost, row.Mortgage, row.GroupColor)) for index, row in spaces_df.iterrows()]
        return spaces

    def get_space_info(self,location):
        space = self.spaces[location]
        return space