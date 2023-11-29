import random


class HauntedMansionGame:
    def __init__(self, secret_word, max_attempts=6):
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
                "Please enter a word of the same length as the secret word or a single letter.")

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


def get_random_word():
    words = ['specter', 'haunt', 'apparition', 'phantom', 'spirit', 'wraith',
             'poltergeist']
    return random.choice(words)


def play_haunted_mansion_game():
    secret_word = get_random_word()
    game = HauntedMansionGame(secret_word)

    print("Welcome to the Haunted Mansion!")
    print(
        f"You have {game.max_attempts} attempts to guess the secret word and unlock the hidden passage.")
    print(game.display_word())

    while not game.is_game_over():
        guess = input("Enter your guess: ")
        game.check_guess(guess)
        print(game.display_word())

        if game.is_winner():
            print(
                "Congratulations! You guessed the word and unlocked the hidden passage.")
            return 1

        if game.is_game_over():
            print(
                f"Sorry, you're out of attempts. The word was '{secret_word}'.")
            return 0


class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    def get_user_choice(self):
        while True:
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            if user_choice in self.choices:
                return user_choice
            else:
                print("Invalid choice. Please enter rock, paper, or scissors.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        else:
            return "Man at door wins!"

    def play_game(self):
        print("Welcome to Rock, Paper, Scissors!")
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f"You chose {user_choice}. Computer chose {computer_choice}.")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)


class Riddle:
    def __init__(self):
        self.answer = ""

    def display_riddle(self):
        print("Solve the riddle to continue")
        file = open('riddle.txt', 'r')
        content = file.readline()
        print(content)
        file.close()
        file_2 = open('riddle_answer.txt','r')
        self.answer = file_2.readline()
        file_2.close()





