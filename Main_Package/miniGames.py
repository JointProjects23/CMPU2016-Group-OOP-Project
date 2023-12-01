import random

import random

class HauntedMansionGame:
    def __init__(self, secret_word, max_attempts=6):
        self.secret_word = secret_word.lower()
        self.max_attempts = max_attempts
        self.remaining_attempts = max_attempts
        self.guessed_letters = set()
        self.incorrect_guess_count = 0  # Track incorrect guesses
        self.five_letter_incorrect_count = 0  # Track incorrect guesses for 5-letter words

    def display_word(self):
        revealed_word = ''
        for i, letter in enumerate(self.secret_word):
            if letter in self.guessed_letters or self.five_letter_incorrect_count > 0:
                revealed_word += letter + ' '
            else:
                revealed_word += '_ '
        return revealed_word.strip()

    def check_guess(self, guess):
        guess = guess.lower()
        if len(guess) == 1 and guess.isalpha():
            print("Single letters are not allowed. Please enter a 5-letter word.")
        elif len(guess) == len(self.secret_word) and guess.isalpha():
            self.check_word(guess)
        else:
            print("What could the word possibly be? "
                  "(Please input a 5-letter word or a single letter):")

    def check_letter(self, guess):
        if guess in self.guessed_letters:
            print("STOP GUESSING THE SAME LETTER DETECTIVE.")
            return

        self.guessed_letters.add(guess)
        self.remaining_attempts -= 1

        if guess not in self.secret_word:
            self.incorrect_guess_count += 1
            print(f"'{guess}' Tis not the letter, Detective. "
                  f"Incorrect guesses: {self.incorrect_guess_count}")
            if self.incorrect_guess_count >= 5:
                print("You can no longer venture here, Detective.")
        else:
            print(f"'{guess}' Well done...Detective")

    def check_word(self, guess):
        if len(guess) == 5:
            # Check for 5-letter word
            if guess == self.secret_word:
                self.guessed_letters = set(self.secret_word)
                print("Correct word! Well done...Detective")
            else:
                self.incorrect_guess_count += 1
                self.five_letter_incorrect_count += 1

                print(f"'{guess}' is not the correct word, Detective. "
                      f"Incorrect guesses: {self.incorrect_guess_count}")

                if self.five_letter_incorrect_count >= 5:
                    print("You can no longer venture here, Detective.")
                    self.remaining_attempts = 0
                else:
                    print("You can try again, Detective.")
                    self.remaining_attempts -= 1

        else:
            # Handle incorrect guess for non-5-letter words
            for letter in guess:
                if letter in self.secret_word and letter not in self.guessed_letters:
                    print(f"'{letter}' is a letter in the word, getting "
                          f"close Detective.")
                    self.guessed_letters.add(letter)
                elif letter not in self.secret_word:
                    self.incorrect_guess_count += 1
                    print(f"'{letter}' Tis not in the word Detective. "
                          f"Incorrect guesses: {self.incorrect_guess_count}")
                    if self.incorrect_guess_count >= 5:
                        print("You can no longer venture here, Detective.")
                        self.remaining_attempts = 0
                    else:
                        self.remaining_attempts -= 1

    def is_winner(self):
        return set(self.secret_word) == self.guessed_letters

    def is_game_over(self):
        return self.remaining_attempts <= 0 or self.incorrect_guess_count >= 5

    def get_random_word(self):
        words = ['specter', 'haunt', 'apparition', 'phantom', 'spirit',
                 'wraith', 'poltergeist']
        return random.choice(words)

    def play_haunted_mansion_game(self):
        print("\nThis takes you back for a moment; you ponder your choices and decide "
              "it's for the best to listen to the inscription on the wall.\n"
              "What word could it possibly be? Maybe there are clues elsewhere?")
        print(
            f"\nCareful detective, you only have {self.max_attempts} guesses "
            f"to venture down this passageway.")
        print(self.display_word())

        while not self.is_game_over():
            guess = input("What is your guess, Detective: ")
            self.check_guess(guess)
            print(self.display_word())

            if self.is_winner():
                print(
                    f"Surprise, Surprise! You actually got it right, "
                    f"Detective...You begin to pass through the passageway, "
                    f"confident in your abilities to solve this mystery.")
                return 1

            if self.is_game_over():
                print(
                    f"You are suddenly pushed back from the passageway. "
                    f"The word \"{self.secret_word}\" echoes through the hallway. "
                    f"You have guessed the word wrong, and you begin to realize "
                    f"going back through the passageway is not possible.")
                return 0

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.attempts = 3

    def get_user_choice(self):
        while True:
            user_choice = input("What is your choice Detective, rock, paper, "
                                "or scissors: "
                                "").lower()
            if user_choice in self.choices:
                return user_choice
            else:
                print("What was that detective? Pick only rock, paper, "
                      "or scissors!!!")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "We picked the same, interesting Detective"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            return "You've won, proceed ahead..."
        else:
            return "Silly little Detective"

    def play_game(self):
        print("This game is Rock, Paper, Scissors Detective!"
              "You have 3 tries, or I take your HEAD!!!")
        while self.attempts > 0:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(
                f"You chose {user_choice} Detective. I chose"
                f"{computer_choice}.")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            if result == "You've won, proceed ahead...":
                print(
                    "You've proven your worth in the game of Rock, Paper, Scissors."
                    "Proceeding ahead to the next challenge..."
                )
                break
            else:
                self.attempts -= 1
                print(f"You have {self.attempts} chances left Detective")


class Riddle:
    def __init__(self):
        self.line = random.randint(0, 4)
        self.__answer = self.openfile("riddle_answer.txt")
        self.riddle = self.openfile("riddle.txt")

    def openfile(self, filename):
        with open(filename, 'r') as file:
            items_list = file.readlines()
        return items_list[self.line]

    def print_riddle(self):
        print(self.riddle)

    @property
    def get_answer(self):
        return self.__answer
