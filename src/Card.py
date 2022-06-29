# Card represents an entity carrying a string to be acted on
# In Monopoly, examples would be Chance and Community Chest Cards

class Card(object):

    def __init__(self, card_type, action):
        self.set_card_type(card_type)
        self.set_action(action)

    def set_card_type(self, card_type):
        self.card_type = card_type

    def set_action(self, action):
        self.action = action

    def get_card_type(self):
        return self.card_type

    def get_action(self):
        return self.action
