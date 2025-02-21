def get_name():
    name = ""
    while len(name) == 0:
        name = input("Enter your name: ")
    return name

def welcome(name):
    return "Hello " + name + " and welcome to the World of Games (WoG)\nHere you can find many cool games to play"

def load_game():
    print("\nPlease choose a game to play:\n",
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n",
          "2. Guess Game - guess a number and see if you chose like the computer\n",
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n",
          "4. Exit\n")

def select_game():
    game = 0
    while not 1 <= game <= 4:
        try:
            game = int(input("Which game would you like to play? "))
        except ValueError:
            continue
    return game

def select_difficulty():
    difficulty = 0
    while not 1 <= difficulty <= 5:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
        except ValueError:
            continue
    return difficulty