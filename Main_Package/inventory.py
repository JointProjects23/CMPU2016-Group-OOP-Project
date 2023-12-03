# inventory.py

class Inventory:
    """The Inventory class manages the player's inventory."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the inventory."""
        self.items.append(item)
        print(f"You added {item.name} to your inventory.")

    def use_item(self, item_name, game):
        """Use an item from the inventory."""
        item = next((item for item in self.items if item.name.lower() == item_name.lower()), None)
        if item:
            item.use(game)  # Corrected from apply_effect to use
            self.items.remove(item)
            print(f"{item.name} has been removed from your inventory.")
        else:
            print(f"You don't have {item_name} in your inventory.")