import json

class Leaderboard:
    def __init__(self):
        self._scores = {}

    def add_player(self, player_name):
        if player_name not in self._scores:
            self._scores[player_name] = {"score": 0}

    def update_score(self, player_name, score):
        if player_name in self._scores:
            self._scores[player_name]["score"] += score

    def get_top_players(self, num_players=5):
        sorted_scores = sorted(self._scores.items(), key=lambda x: x[1]["score"], reverse=True)
        return sorted_scores[:num_players]

    def save_leaderboard(self, filename):
        with open(filename, 'w') as file:  # Change 'a' to 'w'
            json.dump(self._scores, file, indent=2)

    def load_leaderboard(self, filename):
        leaderboard = Leaderboard()
        try:
            with open(filename, 'r') as file:
                leaderboard._scores = json.load(file)
        except FileNotFoundError:
            pass
        return leaderboard

