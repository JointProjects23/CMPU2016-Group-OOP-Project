import json


class Leaderboard:
    def __init__(self):
        """
        Initialize an empty leaderboard.

        Parameters:
        None

        Returns:
        None
        """
        self._scores = {}

    def update_score(self, player_name, score):
        """
        Update the score of a player.

        Parameters:
        - player_name (str): The name of the player whose score is being updated.
        - score (int): The amount by which to update the player's score.

        Returns:
        None
        """
        if player_name in self._scores:
            self._scores[player_name] += score

    def get_top_players(self, num_players=5):
        """
        Retrieve the top players based on their scores.

        Parameters:
        - num_players (int): The number of top players to retrieve (default is 5).

        Returns:
        list: A list of tuples containing player names and their corresponding scores.
        """
        sorted_scores = sorted(self._scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores[:num_players]

    def load_leaderboard(self, filename):
        """
        Load a leaderboard from a file.

        Parameters:
        - filename (str): The name of the file from which to load leaderboard data.

        Returns:
        Leaderboard: A new instance of the Leaderboard class with data loaded from the file.
        """
        leaderboard = Leaderboard()
        user_data = {}  # Initialize an empty dictionary
        try:
            with open(filename, 'r') as file:
                user_data = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist yet or is empty, return an empty leaderboard
            pass

        for player, info in user_data.items():
            if "name" in info and "score" in info:
                leaderboard._scores[info["name"]] = info["score"]

        return leaderboard

