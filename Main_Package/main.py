from game import Game
from leaderboard import Leaderboard

if __name__ == "__main__":
    game = Game()
    game.run()
    # Using the logger
    # print("\nGame Logs:")
    # for log in game.log.logs:
    #     print(log)
    # print("\nGame Error Logs:")
    # for log in game.error_log.lsogs:
    #     print(log)
    game_leaderboard = Leaderboard()
    game_leaderboard = game_leaderboard.load_leaderboard("LeaderboardFile.txt")

    top_players = game_leaderboard.get_top_players()
    for player, score in top_players:
        print(f"{player}: {score}")