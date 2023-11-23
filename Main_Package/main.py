from Main_Package.game import Game

if __name__ == "__main__":
    game = Game()
    game.run()
    # Using the logger
    print("\nGame Logs:")
    for log in game.log.logs:
        print(log)
    print("\nGame Error Logs:")
    for log in game.error_log.logs:
        print(log)

    hello
