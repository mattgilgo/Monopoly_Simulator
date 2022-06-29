import Card

class Chance(Card):

    def __init__(self, action, card_type="Community Chest"):
        super().__init__(card_type, action)
        