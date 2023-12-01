import json
from game import Game
from leaderboard import Leaderboard
import json

if __name__ == "__main__":
    # with open("user_data.json", 'r') as file:
    #     data = json.load(file)
    #
    # # Initialize dictionaries for leaderboard and player info
    # leaderboard = {}
    # player_info = {}
    #
    # try:
    #     # Iterate through the data to separate into leaderboard and player info dictionaries
    #     for player, info in data.items():
    #         player_info[player] = {
    #             "hashed_password": info["hashed_password"],
    #             "Score": info["Score"]
    #         }
    #
    #         leaderboard[player] = info["Score"]
    #
    # # Display the separated dictionaries
    # print("Player Info:")
    # print(json.dumps(player_info, indent=2))

    # print("\nLeaderboard:")
    # print(json.dumps(leaderboard, indent=2))
    game = Game()
    game.run()
    game_leaderboard = Leaderboard() # creates a new empty instance of
    # leaderboard class
    game_leaderboard = game_leaderboard.load_leaderboard(
        "user_data.json") # saves the file to the leaderboard instance

    top_players = game_leaderboard.get_top_players() # gets top players from
    # leaderboard, saved as dictionary
    for player, score in top_players:

        print(f"{player}: {score}")
