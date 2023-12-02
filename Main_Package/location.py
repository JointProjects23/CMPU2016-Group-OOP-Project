from character import NPC
import json


class Location:
    def __init__(self, number_of_clues):
        """
        Initialize a Location instance.

        Parameters:
        - number_of_clues (int): The total number of clues available in the location.

        Returns:
        None
        """
        self._visited = False
        self._all_clues_found = False
        self.number_of_clues_to_find = number_of_clues
        self.__clues = []
        self.clues_found = len(self.__clues)

    @property
    def visited(self):
        """
        Get the visited status of the location.

        Returns:
        bool: True if the location has been visited, False otherwise.
        """
        return self._visited

    @visited.setter
    def visited(self, value):
        """
        Set the visited status of the location.

        Parameters:
        - value (bool): The boolean value to set as the visited status.

        Returns:
        None
        """
        if isinstance(value, bool):
            self._visited = value
        else:
            print("Variable is expected to be a boolean.")

    @property
    def all_clues_found(self):
        """
        Get the status of whether all clues in the location have been found.

        Returns:
        bool: True if all clues have been found, False otherwise.
        """
        return self._all_clues_found

    @all_clues_found.setter
    def all_clues_found(self, value):
        """
        Set the status of whether all clues in the location have been found.

        Parameters:
        - value (bool): The boolean value to set as the all_clues_found status.

        Returns:
        None
        """
        if isinstance(value, bool):
            self._all_clues_found = value
        else:
            print("Variable is expected to be a boolean.")

    def add_clue(self, clue):
        """
        Add a clue to the location.

        Parameters:
        - clue (str): The clue to add to the location.

        Returns:
        None
        """
        self.__clues.append(clue)

    def review_clue(self):
        """
        Retrieve all clues in the location.

        Returns:
        list: A list of clues available in the location.
        """
        return self.__clues

    @property
    def interact_with_npcs(self):
        """
        Get the NPC interaction method of the location.

        Returns:
        function: The NPC interaction method.
        """
        return self.npc.interact

    @property
    def npc_action(self):
        """
        Get the NPC action in the location.

        Returns:
        set: A set containing the NPC's action.
        """
        return {self.npc.action}

    def import_past_progress(self, loaction_data):
        for clues in loaction_data["Clues"]:
            self.__clues.append(clues)
        self.all_clues_found = loaction_data["All clues found"]


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

    def interact_with_npcs(self):
        pass


class Kitchen(Location):
    def __init__(self):
        super().__init__(3)
        self._visited = False
        self._all_clues_found = False
        self.npc = NPC("Smelly Chef", "Get out of my Kitchen", "Goes back to "
                                                               "cooking", 69)


class Library(Location):
    def __init__(self):
        super().__init__(5)
        self.visited = False
        self.all_clues_found = False
        self.npc = NPC("Librarian", "SHHHH", "Goes back to "
                                             "reading", 50)


class Attic(Location):
    def __init__(self):
        super().__init__(2)
        self.visited = False
        self.all_clues_found = False

        self.npc = NPC("Laura", "Hello how are you", "Goes back to "
                                                     "writing her journal", 15)
