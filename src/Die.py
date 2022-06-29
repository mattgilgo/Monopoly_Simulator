from random import randint

# Class to make die for rolling
class Die(object):
    
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.value = 0
    
    def roll_die(self):
        self.value = randint(self.min_value, self.max_value)

    def get_die_value(self):
        return self.value
    