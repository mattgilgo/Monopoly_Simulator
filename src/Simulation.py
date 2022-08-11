import Monopoly
import pandas as pd
from datetime import datetime



# Class for simulation

class Simulator:

    def __init__(self, num_players, num_games):
        self.num_players = num_players
        self.num_games = num_games
        self.results = []
    
    def run_sim(self):
        for i in self.num_games:
            game = Monopoly(self.num_players)
            result = game.run()
            self.results.append(result)
        results_df = pd.toFrame(self.results)
        time = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
        results_df.to_csv('sim_results/monopoly_sim_'+time+".csv")
