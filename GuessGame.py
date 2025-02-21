import random


class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        """Generates a random number between 1 and difficulty."""
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        """Prompts the user for a valid number between 1 and difficulty."""
        while True:
            try:
                guess = int(input(f"Enter a number between 1 and {self.difficulty}: "))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print(f"Please enter a number within the range 1 to {self.difficulty}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def compare_results(self, guess):
        """Compares the guessed number with the secret number."""
        if guess == self.secret_number:
            print("Congratulations! You've guessed the number correctly.")
            return True
        else:
            print(f"Sorry, the correct number was {self.secret_number}.")
            return False

    def play(self):
        """Plays the guessing game."""
        self.generate_number()
        guess = self.get_guess_from_user()
        return self.compare_results(guess)


def guess_game(difficulty):
    return GuessGame(difficulty).play()


if __name__ == "__main__":
    guess_game(int(input("Set the difficulty level (1-5): ")))