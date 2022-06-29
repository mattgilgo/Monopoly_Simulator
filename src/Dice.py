from random import randint
import Die

# Class to make a group of dice
class Dice([Die]):

    def __init__(self, dies):
        self.dies = dies
