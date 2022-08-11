from random import randint
import Die

# Class to make a group of dice
class Dice([Die]):

    def __init__(self, dies):
        self.dies = dies

    def roll_dice(self):
        for die in self.dies:
            die.roll_die()
        value = self.get_dice_val()
        doubles = self.are_dice_doubles()
        return value, doubles
    
    def get_dice_val(self):
        dice_val = 0
        for die in self.dies:
            dice_val = dice_val + die.value
        return dice_val
    
    def are_dice_doubles(self):
        die1_val = self.dies[0].value
        die2_val = self.dies[1].value
        if die1_val == die2_val:
            return True
        else:
            return False