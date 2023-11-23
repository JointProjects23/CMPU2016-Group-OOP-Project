from Main_Package.crimeScene import CrimeScene
from Main_Package.loggable import Loggable
from Main_Package.character import Suspect
from Main_Package.character import NPC
from Main_Package.character import Witness
from Main_Package.leaderboard import Leaderboard



# Define the main game class
class Game:
    """The Game class is set up to manage the game's behavior."""

    def __init__(self):
        self.game_log = Loggable()
        self.__error_logger = Loggable()
        self.running = True
        self.started = False
        self.characters_interacted = False
        self.npcs_interacted = False
        self.score = 0
        self.crime_scene = CrimeScene("Mansion's Drawing Room")
        self.witness = Witness(
            "Lady Victoria Starling",
            "I cant believe my Diamond necklace was"
            " Stolen!\nI heard someone in my room last night",
            "Someone in the owners room last night",
            "walks away",
            78,
        )
        self.witness2 = Witness(
            "Ms. Parker",
            "I saw someone near the window at the " "time of the incident.",
            "Suspicious figure in dark clothing.",
            "frustratedly walks away",
            45,
        )
        self.suspect = Suspect(
            "Mr. Reginald ",
            "I was working last night but left at 8",
            "Claims to have left at 8",
            "walks away in a rush",
            61,
        )
        self.npcs = [
            NPC(
                "Beatrice",
                "How do you do.",
                "decides to hang around and see what will happen",
                68,
            ),
            NPC("Seamus", "Welcome to the mansion", "decides to walk away", 29),
            NPC("The Child", "Go away this is my house!", "angrily storms away", 8),
        ]

        self.doors_checker = [False] * 3
        self.doors = ["Kitchen door", "Basement door", "Library door"]

    def __score__(self):
        score = 0
        # this gives you 10 points for interacting with a witness
        if self.witness.interacted:
            score += 10

        # this gives you 10 points for interacting with a witness
        if self.witness2.interacted:
            score += 10

        # this gives you 15 points for interacting with a suspect
        if self.suspect.interacted:
            score += 15

        # this gives you 2 points for interacting with NPCs
        if self.npcs_interacted:
            score += 2

        # this gives you a point for every clue you find
        if self.crime_scene.review_clue():
            score += len(self.crime_scene.review_clue())

        return score

    @property
    def log(self):
        # to do: think of some appropriate access checks here. For example,
        # only admins are allowed to read out logs.
        return self.game_log

    @property
    def error_log(self):
        return self.__error_logger

    def run(self):
        print(
            "Welcome to 'The Poirot Mystery'\n"
            "You are about to embark on a thrilling "
            "adventure as a detective\n"
            "Your expertise is needed to solve a complex case "
            "and unveil the truth\n"
        )

        while self.running:
            try:
                self.update()
            except ValueError as ve:
                self.__error_logger.log(f"Error found:\n {ve}.")
            except Exception as e:
                self.__error_logger.log("Unexpected error from run():\n{e}.")
                print(
                    "Unexpected caught error during running of the Game. "
                    "We continue playing..."
                )
            else:
                self.game_log.log("Successfully updating")
            finally:
                self.game_log.log("---")
        self.end_game()

    def update(self):
        """The update method waits for player input and responds to their
         choice to start the game or quit."""

        if self.started:
            player_input = input(
                "Press 'q' to quit, 'c' to continue,"
                "'i' to interact with characters, 'e' to examine clues at "
                "Crime Scene,"
                "'r' to review your clues,"
                "'d' to choose a door"
                ", or 's' to see your current score"
            )

            self.game_log.log(f"Player input is {player_input}.")

            if player_input.lower() == "q":
                print("exiting...")
                self.running = False
                self.game_log.log("Player quit the game")
            elif player_input.lower() == "c":
                self.continue_game()
                self.game_log.log("Player continued the game")
            elif player_input.lower() == "i":
                character_choice = input(
                    "If you want to speak to the witness and a suspect, "
                    "choose 1. "
                    "If you'd like to speak to other people in the room, "
                    "choose 2:"
                )
                self.game_log.log("Player chose to interact with characters")
                if character_choice == "1":
                    self.game_log.log(
                        "Player chose to interact with witness " "and suspects"
                    )
                    self.interact_with_characters()
                elif character_choice == "2":
                    self.game_log.log("Player chose to interact with NPCs")
                    self.interact_with_npcs()
            elif player_input.lower() == "e":
                self.game_log.log("Player chose to examine clues at " "Crime Scene")
                self.examine_clues()
            elif player_input.lower() == "r":
                self.game_log.log("Player chose to review clues " "at Crime Scene")
                if self.crime_scene:
                    clues = self.crime_scene.review_clue()
                    if clues:
                        print("You review your clues:")
                        for clue in clues:
                            print(clue)
                    else:
                        print("No clues have been gathered yet.")
                        self.game_log.log("Player had no clues to review")
            elif player_input.lower() == "d":
                self.door_choice()
            elif player_input.lower() == "s":
                self.game_log.log("Player chose to see their score")
                print(f"Your current score is {self.__score__()}")
            else:
                raise ValueError("Incorrect user entry.")

        else:
            player_input = input("Press 'q' to quit or 's' to start: ")
            if player_input.lower() == "q":
                self.game_log.log("Player chose to quit the game")
                print("exiting...")
                self.running = False
            elif player_input.lower() == "s":
                self.game_log.log("Player chose to start the game")
                self.started = True
                self.start_game()
            else:
                raise ValueError("Incorrect user entry.")

    def start_game(self):
        """The start_game method introduces the player
        to the mystery case and sets the scene."""
        player_name = input("Enter your detective's name: ")
        self.game_log.log(f"Player entered their name as {player_name}")
        print(
            f"As the renowned detective, {player_name},\n"
            "you were called in to solve the baffling case of the "
            "missing Diamond Necklace Starlight Serenade\n\n"
            "You have been tasked with finding the missing piece "
            "of the mansion's owner, Lady Victoria Starling!\n"
        )

    def door_choice(self):
        """This method handles the door examination option. User input is
        being handled. The user can make 3 choices: door 1 leads to the
        front door, door 2 leads to the library and door 3 leads to the
        kitchen. Wrong user input is being handled via print-outs for error
        handling."""
        print("You decide to choose a door to investigate:")
        for i, door in enumerate(self.doors, start=1):
            print(f"{i}. {door}")
        player_input = int(
            input("Enter the number of the door you want to investigate: ")
        )

        if 0 < player_input < len(self.doors) + 1:  # for valid entry check
            self.game_log.log(f"Player chose to enter door {player_input}")
            if int(player_input) == 1 and not self.doors_checker[0]:
                self.doors_checker[0] = True
                print(
                    "inside is a small kitchen with a butler making food\n"
                    "you ask him who he is  and he tells you hes the "
                    "the mansion's butler, Mr. Reginald\n"
                    "after talking, you realise he has a suspiciously "
                    "extensive knowledge of the mansion's layout\n"
                )
                self.crime_scene.add_clue(
                    "Mr. Reginald's extensive knowledge " "of the mansion's layout"
                )
            elif int(player_input) == 2 and not self.doors_checker[1]:
                self.doors_checker[1] = True
                print(
                    "You slowly open the door to reveal a...\n"
                    "...a dark corridor which leads you to stairs\n"
                )
                self.crime_scene.add_clue("The letter on the ground")
            elif int(player_input) == 3 and not self.doors_checker[2]:
                print(
                    "You open the library door to reveal a hidden\n"
                    "passage...\n"
                    "What secrets does it hold?"
                )
                self.crime_scene.add_clue("The hidden passage " "behind library door")
                self.doors_checker[2] = True
            else:
                self.game_log.log(
                    f"Player chose to enter door {player_input} "
                    f"but they had already looked inside"
                )
                print(
                    f"You have looked in the {self.doors[player_input - 1]} "
                    f"already."
                )
        else:
            raise ValueError(f"Invalid door choice: {player_input}")

    def interact_with_characters(self):
        if not self.characters_interacted:
            print("You decide to interact with the characters in the room.")

            clue_suspect = self.suspect.interact()
            self.crime_scene.add_clue(clue_suspect)
            print(clue_suspect)  # keep the outputs going
            self.game_log.log(f"{self.suspect.name} interacted with Player")
            self.game_log.log(f"{self.suspect.name} provided clue:" f" {clue_suspect}")

            # this adds the suspect alibi to a variable
            # adds it to the clue list,
            # then prints that and the suspect action
            suspect_alibi = self.suspect.provide_alibi()
            self.crime_scene.add_clue(suspect_alibi)
            print(suspect_alibi)
            print(self.suspect.perform_action())
            self.game_log.log(f"{self.suspect.name} " f"provided alibi: {clue_suspect}")

            clue_witness = self.witness.interact()
            self.crime_scene.add_clue(clue_witness)
            print(clue_witness)
            self.game_log.log(f"{self.witness.name} interacted with Player")
            self.game_log.log(f"{self.suspect.name} " f"provided clue: {clue_suspect}")

            # this adds the witness observation to a variable adds
            # it to the clue list, then prints that and the witness action
            # and changes interacted to true
            witness_observation = self.witness.share_observation()
            self.crime_scene.add_clue(witness_observation)
            print(witness_observation)
            print(self.witness.perform_action())
            self.game_log.log(
                f"{self.suspect.name} " f"provided observation: {clue_suspect}"
            )

            clue_witness = self.witness2.interact()
            self.crime_scene.add_clue(clue_witness)
            print(clue_witness)
            self.game_log.log(f"{self.witness2.name} interacted with Player")
            self.game_log.log(f"{self.suspect.name} " f"provided clue: {clue_suspect}")

            # this adds the witness2 observation
            # to a variable adds it to the clue list, then prints that and
            # the witness action and changes interacted to true
            witness_observation = self.witness2.share_observation()
            self.crime_scene.add_clue(witness_observation)
            print(witness_observation)
            print(self.witness2.perform_action())
            self.characters_interacted = True
            self.game_log.log(
                f"{self.suspect.name} provided observation:" f" {clue_suspect}"
            )

            # this compares the age of the 2 witnesses
            print(self.witness < self.witness2)
        else:
            print(
                "You have already interacted with the characters. \nThey no"
                "longer wish to speak to you."
            )

    def interact_with_npcs(self):
        if self.npcs_interacted:
            print(
                "You have already talked to them they no longer wish to " "talk to you"
            )
            self.game_log.log(
                "Player tried to interact with NPCs but they "
                "already interacted with player "
            )
        else:
            print("You decide to interact some others in the room.")
            for index, npc in enumerate(self.npcs):
                self.game_log.log(f"{npc.name} interacted with Player")
                interaction = npc.interact
                action = npc.perform_action()
                print(f"{interaction}\n{action}")
                self.game_log.log(f"{npc.name} said to the player:" f" {npc.dialogue}")
            self.crime_scene.add_clue(
                "Three people hanging around the Crime Scene"
                "who have nothing to do with the crime"
            )
            self.npcs_interacted = True
            print(self.npcs[1] < self.npcs[0])

    def examine_clues(self):
        if not self.crime_scene.investigated:
            print(
                "You step into the dimly lit crime scene.\nBroken glass lies "
                "near the window, and a table is overturned.\n"
                "You find a torn piece of fabric near the window.\n"
                "There's a distinct smell of perfume lingering in the air.\n"
                "The mystery deepens."
            )
            self.crime_scene.add_clue("Torn fabric")
            self.crime_scene.add_clue("Broken glass near window")
            self.crime_scene.add_clue("An overturned table at crime scene")
            self.crime_scene.add_clue("Smell of perfume")
            self.crime_scene.investigated = True
        else:
            print(
                "You have already investigated the Crime Scene (Use 'r' to "
                "review the clues gathered)"
            )

    def continue_game(self):
        print("You continue your investigation, determined to solve the " "mystery...")

    def end_game(self):
        # Finds the score from the magic method score
        final_score = self.__score__()

        log_filename = input("Please enter a filename to save the logs:")
        self.log.save_logs_to_file(log_filename)

        print(f"Game Over! Your final score was {final_score}")
        self.game_log.log(
            f"Player ended the game with a final score of" f" {final_score}"
        )
        if final_score > 35:
            print("Well done, that's impressive!!")
        else:
            print("That's disappointing... expected better from you")
