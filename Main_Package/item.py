"""
item.py

This module defines the Item class, representing items that can impact the game.

Author: [Your Name]
Date: [Current Date]

Usage:
    # Example usage of the Item class
    item = Item(name="Clue from Suspect", description="A crucial clue from a suspect.")
    item.use(game_instance)
"""

class Item:
    """
    The Item class represents an item that can impact the game.
    """

    def __init__(self, name, description):
        """
        Initialize an Item with a name and description.

        :param name: The name of the item.
        :param description: A brief description of the item.
        """
        self.name = name
        self.description = description

    def use(self, game):
        """
        Use the item and define its impact on the game.

        :param game: The game instance on which the item is used.
        """
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
