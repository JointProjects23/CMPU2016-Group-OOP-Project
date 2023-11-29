import random


class HauntedMansionGame:
    def __init__(self, max_attempts=6):
        self.secret_words = open("riddle_answer.txt", 'r').readlines()
        self.line = random.randint(0, 6)
        self.max_attempts = max_attempts
        self.remaining_attempts = max_attempts
        self.guessed_letters = set()

    def display_word(self):
        return ' '.join(
            letter if letter in self.guessed_letters
            else '_' for letter in self.secret_words[self.line])

    def check_guess(self, guess):
        guess = guess.lower()
        if len(guess) == 1 and guess.isalpha():
            self.check_letter(guess)
        elif len(guess) == len(self.secret_words[self.line]) and guess.isalpha():
            self.check_word(guess)
        else:
            print(
                "You may enter a full word or single letter as your guess "
                "Decetive")

    def check_letter(self, guess):
        if guess in self.guessed_letters:
            print("STOP GUESSING THE SAME WORD DETECTIVE.")
            return

        self.guessed_letters.add(guess)
        self.remaining_attempts -= 1

<<<<<<< Updated upstream
        if guess not in self.secret_words[self.line]:
            print(f"'{guess}' is not in the word.")
=======
        if guess not in self.secret_word:
            print(f"'{guess}'Tis not the word, Stupid Detective.")
>>>>>>> Stashed changes
        else:
            print(f"'{guess}'Well done...Detective")
            return 1

    def check_word(self, guess):
        if guess == self.secret_words[self.line]:
            self.guessed_letters = set(self.secret_words[self.line])
        else:
            for letter in guess:
<<<<<<< Updated upstream
                if letter in self.secret_words[self.line] and letter not in self.guessed_letters:
                    print(f"'{letter}' is in the word.")
                    self.guessed_letters.add(letter)
                elif letter not in self.secret_words[self.line]:
                    print(f"'{letter}' is not in the word.")
=======
                if letter in self.secret_word and letter not in self.guessed_letters:
                    print(f"'{letter}' is a letter in the word, getting "
                          f"close Detective.")
                    self.guessed_letters.add(letter)
                elif letter not in self.secret_word:
                    print(f"'{letter}' Tis not in the word Detective.")
>>>>>>> Stashed changes
                    self.remaining_attempts -= 1

    def is_winner(self):
        return set(self.secret_words[self.line]) == self.guessed_letters

    def is_game_over(self):
        return self.remaining_attempts <= 0

    def get_random_word(self):
        words = ['specter', 'haunt', 'apparition', 'phantom', 'spirit',
                 'wraith',
                 'poltergeist']
        return random.choice(words)

    def play_haunted_mansion_game(self):
        print("Wanna Play a guessing game Detective??\nWhat word could i "
              "possibly be thinking of...")
        print(
            f"\nCareful detective you only have {self.max_attempts} guesses "
            f"for my word"
            f" to unlock the hidden passage.")
        print(self.display_word())

        while not self.is_game_over():
            guess = input("What is your guess Detective:")
            self.check_guess(guess)
            print(self.display_word())

            if self.is_winner():
                print(
<<<<<<< Updated upstream
                    "Congratulations! You guessed the word and unlocked the "
                    "hidden passage.")
                return True
=======
                    f"Suprise Surpise you actually got it right "
                    f"Detective...You may enter")
                return 1
>>>>>>> Stashed changes

            if self.is_game_over():
                print(
                    f"Get out of here Detective, MY WORD WAS '"
                    f"{self.secret_word}'.")
                return False


class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.attempts = 3

    def get_user_choice(self):
        while True:
            user_choice = input("What is your choice Detective rock, paper, "
                                "or scissors: "
                                "").lower()
            if user_choice in self.choices:
                return user_choice
            else:
                print("What was that detective.pick only rock, paper, "
                      "or scissors!!!")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice, attempts):
        if user_choice == computer_choice:
<<<<<<< Updated upstream
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
=======
            return "We picked the same, interesting Detective"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            return "You've won detective, proceede ahead..."
        else:
            return "Silly little Detective"
>>>>>>> Stashed changes

    def play_game(self):
        print("This game is Rock, Paper, Scissors Detective!"
              "You have 3 tries, or I take your HEAD!!!")
        while self.attempts > 0:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(
<<<<<<< Updated upstream
                f"You chose {user_choice}. Computer chose {computer_choice}.")
            result = self.determine_winner(user_choice, computer_choice,
                                           self.attempts)
            print(result)
            if result == "You win!":
                return True
            print(f"You have {self.attempts} left")
        return False
=======
                f"You chose {user_choice} Detective. I chos"
                f"e {computer_choice}.")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            if result == "You win Detective":
                break
            print(f"You have {self.attempts} chnaces left Detective")
>>>>>>> Stashed changes


class Riddle:
    def __init__(self):
        self.__answer = open("riddle_answer.txt", 'r').readlines()
        self.riddle = open('riddle.txt', 'r').readlines()
        self.line = random.randint(0, 4)

    def print_riddle(self):
        print(self.riddle[self.line])

    @property
    def get_answer(self):
<<<<<<< Updated upstream
        return self.__answer[self.line]

=======
        return self.__answer
>>>>>>> Stashed changes
