# Define an abstract base class for a crime scene
class CrimeScene:
    def __init__(self, location):
        self.__investigated = False
        self.location = location
        self.__clues = []

    # Define a property to get the logs
    @property
    def investigated(self):
        return self.__investigated

    @investigated.setter
    def investigated(self, value):
        if isinstance(value, bool):
            self.__investigated = value
        else:
            print("investigated is expected to be a boolean.")

    def add_clue(self, clue):
        self.__clues.append(clue)

    def review_clue(self):
        return self.__clues
