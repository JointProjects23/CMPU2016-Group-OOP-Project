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

riddle = Riddle()
riddle.display_riddle()

print("Enter your answer here :")
user_input = input()

if user_input.lower() == riddle.answer.lower():
    print("You guessed correctly")
else:
    print("You guessed incorrectly")


