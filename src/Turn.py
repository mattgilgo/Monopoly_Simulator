import Player
import Dice
import Die
import MonopolyBoard

# class representing a turn in Monopoly

class Turn(Player):

    def __init__(self, player, monopoly_board):
        self.player = player
        self.dice = [Dice(Die(1,6),Die(1,6))]
        self.monopoly_board = monopoly_board

    def take_turn(self):
        # Let player buy house for most expensive property if funds are sufficient
        if (len(self.player.properties) > 0) & (self.player.money > 1000):
            buy_home_for = ""
            prop_val = 0
            for property in self.player.properties:
                if prop_val < property.purchase_value:      # Add in logic to make player buy 1 house for each color before adding a second house to property
                    prop_val = property.purchase_value
                    buy_home_for = property
            buy_home_for.add_homes(1)                       

        roll_val, doubles = self.dice.roll_dice()
        self.player.move_player(roll_val)
        space = self.monopoly_board.get_space_info(self.player.location)
        if space.purchase_value > 0:
            if space.owned == False:
                if self.player.money > space.purchase_value:
                    if space.space_type == "Property":
                        self.player.add_property(space)
                    elif space.space_type == "Railroad":
                        self.player.add_railroad(space)
                    else:
                        self.player.add_utility(space)
                    self.monopoly_board[space].owned = True
                    self.monopoly_board[space].owner = self.player
            else:   # Update later to account for utilities and railroads
                if space.space_type == "Property":
                    player_to_pay = space.owner
                    owed_rent = space.rent
                    self.player.money -= owed_rent
                elif space.space_type == "Railroad":
                    player_to_pay = space.owner
                    how_many_rrs = len(player_to_pay.railroads)
                    if how_many_rrs == 1:
                        owed_rent = 25
                        self.player.money -= owed_rent
                    if how_many_rrs == 2:
                        owed_rent = 50
                        self.player.money -= owed_rent
                    if how_many_rrs == 3:
                        owed_rent = 100
                        self.player.money -= owed_rent
                    else:
                        owed_rent = 200
                        self.player.money -= owed_rent
                else:
                    player_to_pay = space.owner
                    how_many_utils = len(player_to_pay.utilities)
                    if how_many_utils == 1:
                        owed_rent = roll_val * 4
                        self.player.money -= owed_rent
                    else:
                        owed_rent = roll_val * 10
                        self.player.money -= owed_rent

        elif space.space_type == "FreeParking":
            amount_in_fp = self.monopoly_board.free_parking
            self.player.money = self.player.money + amount_in_fp
            self.monopoly_board.free_parking = 0
        elif space.space_type == "Tax":
            owed_tax = space.rent
            self.monopoly_board.free_parking += owed_tax
            self.player.money -= owed_tax
        elif space.space_type == "Go":
            self.player.money += 200
        elif space.space_type == "Jail":
            self.player.location = 9
        elif space.space_type == "Chance":
            

        # Code logic for passing Go, going to Jail, landing on Chance, and landing on Community Chest
        # Also add logic to remove player if they run out of money
            ## From this, they can mortgage property
            ## If all properties are mortgaged and they still run out: 
            ### Update all their properties to not being owned
            ### Remove them from game
                
        

        return doubles, self.player, self.monopoly_board, player_to_pay, owed_rent


        
        

        

