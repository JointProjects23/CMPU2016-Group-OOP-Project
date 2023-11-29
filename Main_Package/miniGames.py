import random


class HauntedMansionGame:
    def __init__(self, max_attempts=6):
        self.secret_word = secret_word.lower()
        self.max_attempts = max_attempts
        self.remaining_attempts = max_attempts
        self.guessed_letters = set()

    def display_word(self):
        return ' '.join(
            letter if letter in self.guessed_letters else '_' for letter in
            self.secret_word)

    def check_guess(self, guess):
        guess = guess.lower()
        if len(guess) == 1 and guess.isalpha():
            self.check_letter(guess)
        elif len(guess) == len(self.secret_word) and guess.isalpha():
            self.check_word(guess)
        else:
            print(
                "Please enter a word of the same length as the secret word "
                "or a single letter.")

    def check_letter(self, guess):
        if guess in self.guessed_letters:
            print("You've already guessed that letter.")
            return

        self.guessed_letters.add(guess)
        self.remaining_attempts -= 1

        if guess not in self.secret_word:
            print(f"'{guess}' is not in the word.")
        else:
            print(f"'{guess}' is in the word!")
            return 1

    def check_word(self, guess):
        if guess == self.secret_word:
            self.guessed_letters = set(self.secret_word)
        else:
            for letter in guess:
                if letter in self.secret_word and letter not in self.guessed_letters:
                    print(f"'{letter}' is in the word.")
                    self.guessed_letters.add(letter)
                elif letter not in self.secret_word:
                    print(f"'{letter}' is not in the word.")
                    self.remaining_attempts -= 1

    def is_winner(self):
        return set(self.secret_word) == self.guessed_letters

    def is_game_over(self):
        return self.remaining_attempts <= 0

    def get_random_word(self):
        words = ['specter', 'haunt', 'apparition', 'phantom', 'spirit',
                 'wraith',
                 'poltergeist']
        return random.choice(words)

    def play_haunted_mansion_game(self):
        print("Welcome to the Haunted Mansion!")
        print(
            f"You have {self.max_attempts} attempts to guess the secret word "
            f"and unlock the hidden passage.")
        print(self.display_word())

        while not self.is_game_over():
            guess = input("Enter your guess: ")
            self.check_guess(guess)
            print(self.display_word())

            if self.is_winner():
                print(
                    "Congratulations! You guessed the word and unlocked the "
                    "hidden passage.")
                return 1

            if self.is_game_over():
                print(
                    f"Sorry, you're out of attempts. The word was '"
                    f"{self.secret_word}'.")
                return 0


class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.attempts = 3

    def get_user_choice(self):
        while True:
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            if user_choice in self.choices:
                return user_choice
            else:
                print("Invalid choice. Please enter rock, paper, or scissors.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice, attempts):
        if user_choice == computer_choice:
            self.attempts = self.attempts - 1
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            self.attempts = self.attempts - 1
            return "You win!"
        else:
            self.attempts = self.attempts - 1
            return "Man at door wins!"

    def play_game(self):
        print("Welcome to Rock, Paper, Scissors!"
              "You have 3 tries")
        while self.attempts > 0:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(
                f"You chose {user_choice}. Computer chose {computer_choice}.")
            result = self.determine_winner(user_choice, computer_choice,
                                           self.attempts)
            print(result)
            if result == "You win!":
                return True
            print(f"You have {self.attempts} left")
        return False


class Riddle:
    def __init__(self):
        self.__answer = open("riddle_answer.txt", 'r').readlines()
        self.riddle = open('riddle.txt', 'r').readlines()
        self.line = random.randint(0, 4)

    def print_riddle(self):
        print(self.riddle[self.line])

    @property
    def get_answer(self):
        return self.__answer[self.line]

