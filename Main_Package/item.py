# item.py

class Item:
    """The Item class represents an item that can impact the game."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, game):
        """This method defines the impact of using the item on the game."""
        # Do nothing when using the item
        print(f"Using the {self.name} doesn't have any significant impact.")

