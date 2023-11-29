from Main_Package.character import NPC


class Location:
    def __init__(self, number_of_clues):
        self._visited = False
        self.all_clues_found = False
        self.number_of_clues_to_find = number_of_clues


class Kitchen(Location):
    def __init__(self, number_of_clues):
        super().__init__(number_of_clues)
        self._visited = False
        self._all_clues_found = False
        self.npc = NPC("Chef", "Get out of my Kitchen", "Goes back to "
                                                        "cooking", 50)

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, value):
        if isinstance(value, bool):
            self._visited = value
        else:
            print("variable is expected to be a boolean.")

    @property
    def all_clues_found(self):
        return self._all_clues_found

    @all_clues_found.setter
    def all_clues_found(self, value):
        if isinstance(value, bool):
            self._all_clues_found = value
        else:
            print("variable is expected to be a boolean.")


class Library(Location):
    def __init__(self, number_of_clues):
        super().__init__(number_of_clues)
        self.visited = False
        self.all_clues_found = False
        self.npc = NPC("Librarian", "SHHHH", "Goes back to "
                                             "reading", 50)


class Attic(Location):
    def __init__(self, number_of_clues):
        super().__init__(number_of_clues)
        self.visited = False
        self.all_clues_found = False
        self.npc = NPC("Anne", "Hello", "Goes back to "
                                             "wrtiing her journal", 15)
