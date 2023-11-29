# item.py 

class Item:
    """The Item class represents an item that can impact the game."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, game):
        """This method defines the impact of using the item on the game."""
        if self.name == "Clue from Suspect":
            # Modify the game state based on using the clue from the suspect
            print("Using the clue from the suspect reveals additional "
                  "information.")
            game.score += 5  # Adjust the score, for example
            game.suspect_confession = True  # Modify a game attribute
        elif self.name == "NPC Interaction":
            # Modify the game state based on using information from NPCs
            print("Using the information from NPCs helps you uncover a secret.")
            game.score += 3  # Adjust the score, for example
            game.uncover_secret = True  # Modify a game attribute
        elif self.name == "Torn Fabric":
            # Modify the game state based on using the torn fabric clue
            print("Using the torn fabric clue helps you reconstruct the "
                  "sequence of events.")
            game.score += 2  # Adjust the score, for example
            game.reconstruct_sequence = True  # Modify a game attribute
        # Add more conditions based on the specific items and their impact on the game
        else:
            print(f"Using the {self.name} doesn't seem to have any significant impact.")

