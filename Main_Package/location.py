from Main_Package.character import NPC


class Location:
    def __init__(self, number_of_clues):
        self._visited = False
        self.all_clues_found = False
        self.number_of_clues_to_find = number_of_clues
        self.__clues = []

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

    def add_clue(self, clue):
        self.__clues.append(clue)

    def review_clue(self):
        return self.__clues


class CrimeScene(Location):
    def __init__(self, name):
        super().__init__(number_of_clues=28)
        self.__investigated = False
        self.__clues = []
        self.name = name

    @property
    def investigated(self):
        return self.__investigated

    @investigated.setter
    def investigated(self, value):
        if isinstance(value, bool):
            self.__investigated = value
        else:
            print("investigated is expected to be a boolean.")

    def save_clues(self):
        with open("CrimeSceneClues.txt", 'w') as file:
            file.write(f"Location: {self.__class__.__name__}\n")
            file.write(f"All clues found: {self.all_clues_found}\n")


class Kitchen(Location):
    def __init__(self):
        super().__init__(3)
        self._visited = False
        self._all_clues_found = False
        self.npc = NPC("Chef", "Get out of my Kitchen", "Goes back to "
                                                        "cooking", 50)

    def save_clues(self):
        with open("KitchenClues.txt", 'w') as file:
            file.write(f"Location: {self.__class__.__name__}\n")
            file.write(f"All clues found: {self.all_clues_found}\n")


class Library(Location):
    def __init__(self):
        super().__init__(5)
        self.visited = False
        self.all_clues_found = False
        self.npc = NPC("Librarian", "SHHHH", "Goes back to "
                                             "reading", 50)

    def save_clues(self):
        with open("LibraryClues.txt", 'w') as file:
            file.write(f"Location: {self.__class__.__name__}\n")
            file.write(f"All clues found: {self.all_clues_found}\n")


class Attic(Location):
    def __init__(self):
        super().__init__(2)
        self.visited = False
        self.all_clues_found = False
        self.npc = NPC("Anne", "Hello", "Goes back to "
                                        "wrtiing her journal", 15)

    def save_clues(self):
        with open("AtticClues.txt", 'w') as file:
            file.write(f"Location: {self.__class__.__name__}\n")
            file.write(f"All clues found: {self.all_clues_found}\n")
