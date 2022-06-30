from Chance import Chance
from CommunityChest import CommunityChest
import Player
import Board
import Turn
import Piece
import MonopolyBoard


# Class representing a game of Monopoly

class Monopoly:

    def __init__(self, num_players):
        self.num_players = num_players
        self.pieces = [Piece("Top Hat"), Piece("Thimble"), Piece("Iron"), Piece("Shoe"), Piece("Battleship"), Piece("Cannon")]
        self.players = []
        self.board = MonopolyBoard()
        self.chance_deck = Chance.create_chance_deck()
        self.com_chest_deck = CommunityChest.create_com_chest_deck()
    
    def generate_players(self):
        players = []
        for i in range(0, self.num_players):
            player = Player("Player "+str(i), self.pieces[i])
            players = players.append(player)
        return players

    """
    def generate_pieces():
        hat = Piece("Top Hat")
        thimble = Piece("Thimble")
        iron = Piece("Iron")
        shoe = Piece("Shoe")
        battleship = Piece("Battleship")
        cannon = Piece("Cannon")
        pieces = [hat, thimble, iron, shoe, battleship, cannon]
        return pieces
    """

    
    def run(self):

        # Initialize game and players in game
        game = Monopoly(self.num_players)
        game.players = game.generate_players()

        # Set loop to take turns until one winner remains
        while game.players > 1:
            for player in game.players:
                doubles = True
                while doubles == True:
                    doubles, updated_player, updated_board, player_owed_rent, amount_owed_rent = Turn(player, self.board)
                    game.players[player] = updated_player
                    game.board = updated_board 
                    game.players[player_owed_rent].money = amount_owed_rent

        
        # Retrieve data on winner
        winner = game.players[0]
        winner_results = winner.get_data()
        return winner_results





        
