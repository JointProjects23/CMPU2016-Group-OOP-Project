import random

class HauntedMansionGame:
    def __init__(self, secret_word, max_attempts=6):
        """
        Initialize a HauntedMansionGame instance.

        Parameters:
        - secret_word (str): The secret word to be guessed.
        - max_attempts (int): The maximum number of attempts allowed for guessing the word. Default is 6.

        Returns:
        None
        """
        self.secret_word = secret_word.lower()
        self.max_attempts = max_attempts
        self.remaining_attempts = max_attempts
        self.guessed_letters = set()

    def display_word(self):
        """
        Display the current state of the secret word, revealing guessed letters and hiding others.

        Returns:
        str: The formatted secret word display.
        """
        return ' '.join(
            letter if letter in self.guessed_letters else '_' for letter in
            self.secret_word)

    def check_guess(self, guess):
        """
        Check the validity of the guess and update the game state accordingly.

        Parameters:
        - guess (str): The user's guess, either a single letter or a complete word.

        Returns:
        None
        """
        guess = guess.lower()
        if len(guess) == 1 and guess.isalpha():
            self.check_letter(guess)
        elif len(guess) == len(self.secret_word) and guess.isalpha():
            self.check_word(guess)
        else:
            print("You may enter a full word or single letter as your guess")

    def check_letter(self, guess):
        """
        Check a single letter guess and update the game state.

        Parameters:
        - guess (str): The single letter guessed by the user.

        Returns:
        int or None: Returns 1 if the guessed letter is correct, None otherwise.
        """
        if guess in self.guessed_letters:
            print("STOP GUESSING THE SAME WORD DETECTIVE.")
            return

        self.guessed_letters.add(guess)
        self.remaining_attempts -= 1

        if guess not in self.secret_word:
            print(f"'{guess}'Tis not the word, Stupid Detective.")
        else:
            print(f"'{guess}'Well done...Detective")
            return 1

    def check_word(self, guess):
        """
        Check a complete word guess and update the game state.

        Parameters:
        - guess (str): The complete word guessed by the user.

        Returns:
        None
        """
        if guess == self.secret_word:
            self.guessed_letters = set(self.secret_word)
        else:
            for letter in guess:
                if letter in self.secret_word and letter not in self.guessed_letters:
                    print(f"'{letter}' is a letter in the word, getting "
                          f"close Detective.")
                    self.guessed_letters.add(letter)
                elif letter not in self.secret_word:
                    print(f"'{letter}' Tis not in the word Detective.")
                    self.remaining_attempts -= 1

    def is_winner(self):
        """
        Check if the user has guessed the entire word correctly.

        Returns:
        bool: True if the user has guessed the entire word, False otherwise.
        """
        return set(self.secret_word) == self.guessed_letters

    def is_game_over(self):
        """
        Check if the game is over due to reaching the maximum attempts.

        Returns:
        bool: True if the game is over, False otherwise.
        """
        return self.remaining_attempts <= 0

    def get_random_word(self):
        """
        Get a random word from a predefined list.

        Returns:
        str: A random word.
        """
        words = ['specter', 'haunt', 'apparition', 'phantom', 'spirit',
                 'wraith', 'poltergeist']
        return random.choice(words)

    def play_haunted_mansion_game(self):
        """
        Play the Haunted Mansion guessing game.

        Returns:
        int: 1 if the user wins, 0 if the game is lost.
        """
        print("Wanna Play a guessing game Detective??\nWhat word could I "
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
                    f"Surprise, Surprise you actually got it right "
                    f"Detective...You may enter")
                return 1

            if self.is_game_over():
                print(
                    f"Get out of here Detective, MY WORD WAS '"
                    f"{self.secret_word}'.")
                return 0


class RockPaperScissors:
    def __init__(self):
        """
        Initialize a RockPaperScissors instance.

        Returns:
        None
        """
        self.choices = ["rock", "paper", "scissors"]
        self.attempts = 3

    def get_user_choice(self):
        """
        Get the user's choice for Rock, Paper, or Scissors.

        Returns:
        str: The user's choice.
        """
        while True:
            user_choice = input("What is your choice Rock, Paper, "
                                "or Scissors: ").lower()
            if user_choice in self.choices:
                print("Pick only rock, paper, or scissors!!")
                return user_choice

    def get_computer_choice(self):
        """
        Get the computer's random choice for Rock, Paper, or Scissors.

        Returns:
        str: The computer's choice.
        """
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        """
        Determine the winner of the Rock, Paper, Scissors game.

        Parameters:
        - user_choice (str): The user's choice.
        - computer_choice (str): The computer's choice.

        Returns:
        bool: True if the user wins, False otherwise.
        """
        if user_choice == computer_choice:
            print("Draw!!")
            return False
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            return True
        else:
            self.attempts -= 1
            print("Another win for me")
            return False

    def play_game(self):
        """
        Play the Rock, Paper, Scissors game.

        Returns:
        None
        """
        print("This game is Rock, Paper, Scissors!"
              "You have 3 tries, or you are not allowed in!")
        while self.attempts > 0:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(
                f"You chose {user_choice}. I chose "
                f"{computer_choice}.")
            result = self.determine_winner(user_choice, computer_choice)
            if result:
                print("You win!")
                break
            print(f"You have {self.attempts} chances left")


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
