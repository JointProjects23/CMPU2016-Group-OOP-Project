"""
item.py

This module defines the Item class, representing items that can impact the game.

<<<<<<< Updated upstream
Author: Sam Curren, Jamie O'Neill, Hayden Carroll
Date: 15/11/2023 - 01/12/2023

=======
Author: Sam Curran, Jamie O'Neill, Hayden Carroll
Date: 15/11/2023 - 01/12/2023
>>>>>>> Stashed changes

Usage:
    # Example usage of the Item class
    item = Item(name="Clue from Suspect", description="A crucial clue from a suspect.")
    item.use(game_instance)
"""


class Item:
    """
    The Item class represents an item that can impact the game.
    """

    def __init__(self, name, description, impact, score_increase):
        """
        Initialize an Item with a name and description.

        :param name: The name of the item.
        :param description: A brief description of the item.
        """
        self.name = name
        self.description = description
        self.impact = impact
        self.score_increase = score_increase

    def use(self, game):
        """
        Use the item and define its impact on the game.

        :param game: The game instance on which the item is used.
        """

        print(self.impact)
        game.score += self.score_increase

