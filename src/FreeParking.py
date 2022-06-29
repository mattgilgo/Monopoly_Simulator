import Space

# Class representing the Free Parking space in Monopoly

class FreeParking(Space):

    def __init__(self, card_type="Free Parking"):
        super.__init__(self, card_type)
        self.value = 0
    
    def get_value(self):
        return self.value
    
    def reset_value(self):
        self.value = 0

    def add_to_free_parking(self, added_money):
        self.value = self.get_value() + added_money
    
