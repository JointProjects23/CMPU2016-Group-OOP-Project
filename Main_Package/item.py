# item.py

class Item:
    """The Item class represents an item that can impact the game."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, game):
        """This method defines the impact of using the item on the game."""
        if self.name == "Clue from Suspect":
            print("Using the clue from the suspect reveals additional information.")
            game.score += 5
            game.suspect_confession = True
        elif self.name == "NPC Interaction":
            print("Using the information from NPCs helps you uncover a secret.")
            game.score += 3
            game.uncover_secret = True
        elif self.name == "Torn Fabric":
            print("Using the torn fabric clue helps you reconstruct the sequence of events.")
            game.score += 2
            game.reconstruct_sequence = True
        else:
            print(f"Using the {self.name} doesn't seem to have any significant impact.")


