import Card
import pandas as pd
import Deck

class CommunityChest(Card):

    def __init__(self, action, card_type="Community Chest"):
        super().__init__(card_type, action)
    
    def create_com_chest_cards():
        com_chest_df = pd.read_csv('community_chest_cards.csv')
        com_chest_cards = [(CommunityChest(row.Action)) for index, row in com_chest_df.iterrows()]
        return com_chest_cards

    def create_com_chest_deck():
        com_chest_cards = CommunityChest.create_com_chest_cards()
        com_chest_deck = Deck(com_chest_cards)
        return com_chest_deck