from game import Game
from leaderboard import Leaderboard

if __name__ == "__main__":
    game = Game()
    game.run()

    leaderboard_filename = "GameFile.json"  # Update the filename to use JSON

    game_leaderboard = Leaderboard()  # creates a new empty instance of the leaderboard class
    game_leaderboard = game_leaderboard.load_leaderboard(leaderboard_filename)  # loads the file into the leaderboard instance

    top_players = game_leaderboard.get_top_players()  # gets top players from leaderboard, saved as dictionary
    for player, score in top_players:
        print(f"{player}: {score}")

    # Save the leaderboard after the game is finished
    game_leaderboard.save_leaderboard(leaderboard_filename)
