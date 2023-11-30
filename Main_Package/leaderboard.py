class Leaderboard:
    def __init__(self):
        self._scores = {}

    def add_player(self, player_name):
        # Add a new player to the leaderboard with an initial score of 0
        if player_name not in self._scores:
            self._scores[player_name] = 0

    def update_score(self, player_name, score):
        # Update the score of a player
        if player_name in self._scores:
            self._scores[player_name] += score

    def get_top_players(self, num_players=5):
        # Retrieve the top players based on their scores
        sorted_scores = sorted(self._scores.items(), key=lambda x: x[1],
                               reverse=True)
        return sorted_scores[:num_players]

    def save_leaderboard(self, filename):
        with open(filename, 'a') as file:
            for player, score in self._scores.items():
                file.write(f"{player}:{score}\n")

    def load_leaderboard(self, filename):
        leaderboard = Leaderboard()
        try:
            with open(filename, 'r') as file:
                for line in file:
                    player, score = line.strip().split(':')
                    leaderboard._scores[player] = int(score)
        except FileNotFoundError:
            # If the file doesn't exist yet or is empty, return an empty leaderboard
            pass
        return leaderboard
