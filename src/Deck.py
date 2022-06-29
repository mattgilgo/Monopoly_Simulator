import Card
from random import shuffle

# Deck for holding card objects within game

class Deck([Card]):

    def __init__(self, cards):
        self.cards = cards
        self.shuffle()

    def shuffle(self):
        shuffle(self.cards)
    
    def take_card(self):
        top_card = self.stack.pop()
        return top_card