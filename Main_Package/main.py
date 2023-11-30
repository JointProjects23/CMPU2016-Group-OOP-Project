from game import Game
from leaderboard import Leaderboard

if __name__ == "__main__":
    game = Game()
    game.run()
    game_leaderboard = Leaderboard() # creates a new empty instance of
    # leaderboard class
    game_leaderboard = game_leaderboard.load_leaderboard(
        "LeaderboardFile.txt") # saves the file to the leaderboard instance

    top_players = game_leaderboard.get_top_players() # gets top players from
    # leaderboard, saved as dictionary
    for player, score in top_players:

        print(f"{player}: {score}")
