import Simulation

# Main function for Monopoly Simulator

def main():
    num_players = input("Welcome to the Monopoly Simulator! How many players would you like to have playing?\n")
    num_games = input("Great! And how many games would you like them to play?\n")
    print('Perfect! Let the games begin...')
    monopoly_sim = Simulation.Simulator(num_players,num_games)
    monopoly_sim.run_sim()
    print('Simulation Complete!')

if __name__ == '__main__':

    main()
