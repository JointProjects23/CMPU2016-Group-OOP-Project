from abc import ABC, abstractmethod


# Create a Loggable mixin class for logging functionality
class Loggable:
    """In this solution, the Loggable class is incorporated as an independent
    class used for handling logging functionality, and the Game class is
    enhanced to use it via composition. """

    def __init__(self):
        self.__logs = []

    @property
    def logs(self):
        return self.__logs

    def log(self, message):
        if isinstance(message, str):
            self.__logs.append(message)


class CrimeScene:
    # This class has not changed in this lab.
    def __init__(self, location):
        self.location = location
        self.__clues = []
        self.__investigated = False

    @property
    def investigated(self):
        return self.__investigated

    @investigated.setter
    def investigated(self, value):
        self.__investigated = value

    def add_clue(self, clue):
        self.__clues.append(clue)

    def review_clues(self):
        """At the moment there are no checks on who can see the clues. We
        might need some further protection here."""
        return self.__clues


# this class has not changed
class Character(ABC):
    def __init__(self, name, dialogue):
        self._name = name
        self._dialogue = dialogue
        self._interacted = False

    def __str__(self):
        return f"{self.__class__.__name__}: {self._name}"

    def __eq__(self, other):
        if isinstance(other, Character):
            return self._name == other._name
        return False

    def __lt__(self, other):
        if isinstance(other, Character):
            return self._name < other._name
        return False

    @abstractmethod  # Declares an abstract method using a decorator.
    def perform_action(self):
        pass  # Abstract methods never contain any actual logic. The
        # transfer statement "pass" allows for this.

    # An abstract class must contain at least one abstract method.
    # However, "normal" methods may also be contained.
    def interact(self):
        if not self._interacted:
            interaction = f"{self._name}: {self._dialogue}"
            self._interacted = True
        else:
            interaction = f"{self._name} is no longer interested in talking."

        return interaction

    # def has_interacted(self):
    #     return self._interacted


# This class has not changed in this lab
class Suspect(Character):
    def __init__(self, name, dialogue, alibi):
        super().__init__(name, dialogue)
        self._alibi = alibi

    def __repr__(self):
        return f"Suspect('{self._name}', '{self._dialogue}', '{self._alibi}')"

    def provide_alibi(self):
        return f"{self._name}'s Alibi: {self._alibi}"

    def perform_action(self):  # Implement the abstract method for Suspect
        return (f"Suspect {self._name} nervously shifts and avoids eye "
                f"contact.")


# This class has not changed in this lab
class Witness(Character):
    def __init__(self, name, dialogue, observation):
        super().__init__(name, dialogue)
        self._observation = observation

    def __add__(self, other):
        if isinstance(other, Witness):
            combined_observation = f"{self._observation} and {other._observation}"
            combined_name = f"{self._name} and {other._name}"
            return Witness(combined_name, "Combined observations",
                           combined_observation)

    def share_observation(self):
        return f"{self._name}'s Observation: {self._observation}"

    def perform_action(self):  # Implement the abstract method for Witness
        return (f"Witness {self._name} speaks hurriedly and glances around "
                f"anxiously.")


class NPC(Character):
    """
    A class that implements the abstract class Character.
    The perform_action method must provide logic.
    The purpose of this class is to provide characters that are not
    essential for the mystery.
    """

    def perform_action(self):
        return f"{self._name} decides to hang around and see what will happen."

    def interact(self):
        super().interact()
        return "\nI know nothing!"


# Enhanced Game class using composition
class Game:
    def __init__(self):
        # The Logger can be used throughout the game to capture important
        # events, interactions between characters, and observations. The key
        # takeaway is that the Logger class facilitates logging without
        # tightly coupling the game logic with the logging functionality.
        # This promotes modularity and helps in managing dependencies
        # effectively.
        self.__logger = Loggable()

        # ... from before:
        self.__running = True
        self.__game_started = False
        self.__characters_interacted = False  # no double interactions
        self.__npcs_interacted = False  # no double interactions

        self.__crime_scene = CrimeScene("Mansion's Drawing Room")
        self.__suspect = Suspect("Mr. Smith", "I was in the library all "
                                              "evening.",
                                 "Confirmed by the butler.")
        self.__witness = Witness("Ms. Parker", "I saw someone near the window "
                                               "at the time of the incident.",
                                 "Suspicious figure in dark clothing.")
        self.__doors = ["Front door", "Library door", "Kitchen door"]
        self.__doors_checker = [False, False,
                                False]  # avoid using a door again

        self.__clues = []

    @property
    def log(self):
        # to do: think of some appropriate access checks here. For example,
        # only admins are allowed to read out logs.
        return self.__logger

    def run(self):
        # ...
        self.__logger.log("Game started")
        # ...
        print("Welcome to 'The Poirot Mystery'")
        print(
            "You are about to embark on a thrilling adventure as a detective.")
        print(
            "Your expertise is needed to solve a complex case and unveil the truth.")

        while self.__running:
            self.update()

    def update(self):
        # ...
        self.__logger.log("I'm updating")
        # ...

        if not self.__game_started:
            player_input = input("Press 'q' to quit or 's' to start: ")
            if player_input.lower() == "q":
                self.__running = False
            elif player_input.lower() == "s":
                self.__game_started = True
                self.start_game()

            self.__logger.log(f"Player input: {player_input}")

        else:
            player_input = input(
                "Press 'q' to quit, 'c' to continue, 'i' to interact, "
                "'e' to examine clues, 'r' to review clues or 'd' to choose a "
                "door: ")
            if player_input.lower() == "q":
                self.__running = False
            elif player_input.lower() == "c":
                self.continue_game()
            elif player_input.lower() == "i":
                self.interact_with_characters()
            elif player_input.lower() == "e":
                self.examine_clues()
            elif player_input.lower() == "d":
                self.choose_door()
            elif player_input.lower() == "r":
                clues = self.__crime_scene.review_clues()
                if clues:
                    print(clues)
                else:
                    print("You have not found any clues yet.")

            self.__logger.log(f"Player input: {player_input}")

    def start_game(self):
        # ...
        self.__logger.log("Game is starting")
        # ...

        # from before...
        player_name = input("Enter your detective's name: ")
        print(f"Welcome, Detective {player_name}!")
        print(
            "You find yourself in the opulent drawing room of a grand mansion.")
        print(
            "As the famous detective, you're here to solve the mysterious case of...")
        print("'The Missing Diamond Necklace'.")
        print("Put your detective skills to the test and unveil the truth!")

    def interact_with_characters(self):
        """The interact_with_characters method within the Game class
        demonstrates the interaction with characters,
        where each character's dialogue and unique actions (e.g., providing
        an alibi, sharing an observation) are
        displayed. """

        self.__logger.log("Interactions happening: ")

        print("You decide to interact with the characters in the room.")
        character = int(input("If you want to speak to the witness and a "
                              "suspect, "
                              "choose 1. \nIf you'd like to speak to other people in "
                              "the "
                              "room, choose 2: "))

        if character == 1:
            if not self.__characters_interacted:
                self.__logger.log("Interacting with suspects and witnesses.")
                print(
                    "You decide to interact with the witness and suspect in "
                    "the room:")

                clue_suspect = self.__suspect.interact()
                self.__crime_scene.add_clue(clue_suspect)
                print(clue_suspect)  # keep the outputs going

                suspect_alibi = self.__suspect.provide_alibi()
                self.__crime_scene.add_clue(suspect_alibi)
                print(suspect_alibi)

                # use the new abstract method
                print(self.__suspect.perform_action())

                clue_witness = self.__witness.interact()
                self.__crime_scene.add_clue(clue_witness)
                print(clue_witness)

                witness_observation = self.__witness.share_observation()
                self.__crime_scene.add_clue(witness_observation)
                print(witness_observation)

                # use the new abstract method
                print(self.__witness.perform_action())

                self.__characters_interacted = True
            else:
                print(
                    "You have already interacted with the characters. They no "
                    "longer wish to speak to you.")
        elif character == 2:
            if not self.__npcs_interacted:
                self.__logger.log("Interating with people standing about.")
                # Creating and interacting with characters
                print("You decide to speak to other people in the room:")
                indifferent_npc = NPC("Beatrice", "How do you do.")
                friendly_npc = NPC("Seamus", "Welcome to our village.")
                hostile_npc = NPC("Evil Goblin", "Leave this place!")

                characters = [indifferent_npc, friendly_npc, hostile_npc]

                for character in characters:
                    print(character.interact())
                    print(character.perform_action())

                self.__crime_scene.add_clue(
                    "Three people are hanging around the "
                    "scene who have nothing to do with the "
                    "crime.")

                self.__npcs_interacted = True
            else:
                print("People in the room are tied of you. They no longer "
                      "want to speak to you.")
        else:
            print("This was not an option.")

    def examine_clues(self):
        # ...
        self.__logger.log("Examination of clues happening")
        # ...

        # from before...
        print("You decide to examine the clues at the crime scene.")
        if not self.__crime_scene.investigated:
            print("You find a torn piece of fabric near the window.")
            self.__crime_scene.add_clue("Torn fabric")
            self.__crime_scene.investigated = True
        else:
            print("You've already examined the crime scene clues.")

    def choose_door(self):
        # ...
        self.__logger.log("Doors are to be chosen: ")
        # ...

        print("You decide to choose a door to investigate:")

        # nice output to show which door leads to what.
        # human friendly output starts with 1, default would be 0.
        for i, door in enumerate(self.__doors, start=1):
            print(f"{i}. {door}")

        door_choice = int(input("Enter the number of the door you want to "
                                "investigate: "))

        if 0 < door_choice < len(self.__doors) + 1:  # for valid entry check
            if door_choice == 1:
                if not self.__doors_checker[0]:
                    print("As you approach the front door, you hear a faint "
                          "whisper... The plot thickens!")
                    self.__crime_scene.add_clue("faint whisper near kitchen")
                    self.__doors_checker[0] = True
                    self.__logger.log("Front door was chosen.")
                else:
                    print("You have looked in the front door already.")
                    self.__logger.log("Front door was chosen before. No "
                                      "access.")
            elif door_choice == 2:
                if not self.__doors_checker[1]:
                    print("You open the library door to reveal a hidden "
                          "passage... "
                          "What secrets does it hold?")
                    self.__logger.log("The library was chosen.")
                    self.__crime_scene.add_clue("hidden passage behind "
                                                "library door")
                    self.__doors_checker[1] = True
                else:
                    print("You've looked in the library already.")
                    self.__logger.log("The library had been chosen before. "
                                      "No access.")
            elif door_choice == 3:
                if not self.__doors_checker[2]:
                    print("You open the kitchen door. The mansion's chef "
                          "prepares the evening meal. No clues to the mystery "
                          "can be unveiled.")
                    self.__logger.log("The kitchen was chosen.")
                    self.__doors_checker[2] = True
                else:
                    print("You've looked in the kitchen already.")
                    self.__logger.log("The kitchen had been chosen before. "
                                      "No access.")
        else:
            print("Invalid door choice.")
            self.__logger.log("An invalid door choice was made.")

    def continue_game(self):
        print(
            "You continue your investigation, determined to solve the mystery...")
        # ...
        self.__logger.log("Continuing the game.")
        # ...

        # Additional game content and interactions could go here


# Testing the Enhanced Game
if __name__ == "__main__":
    game = Game()
    exec(open('background_picture_game.py').read())
    game.run()
    # Using the logger
    print("\nGame Logs:")
    for log in game.log.logs:
        print(log)
