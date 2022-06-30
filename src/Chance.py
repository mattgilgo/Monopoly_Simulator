import Card
import pandas as pd
import Deck

class Chance(Card):

    def __init__(self, action, card_type="Chance"):
        super().__init__(card_type, action)
        
    def create_chance_cards():
        chance_df = pd.read_csv('chance_cards.csv')
        chance_cards = [(Chance(row.Action)) for index, row in chance_df.iterrows()]
        return chance_cards

    def create_chance_deck():
        chance_cards = Chance.create_chance_cards()
        chance_deck = Deck(chance_cards)
        return chance_deck