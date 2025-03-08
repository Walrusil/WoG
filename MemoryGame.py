import random
import time
from Utils import screen_cleaner


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.sequence = []

    def generate_sequence(self):
        """Generates a list of random numbers between 1 and 101 with length equal to difficulty."""
        self.sequence = [random.randint(1, 101) for _ in range(self.difficulty)]
        print("Remember the following numbers:")
        print(self.sequence)
        time.sleep(0.7)  # Display numbers for 0.7 seconds
        screen_cleaner()  # Clear the console

    def get_list_from_user(self):
        """Prompts the user for a list of numbers."""
        while True:
            try:
                user_input = input(f"Enter {self.difficulty} numbers separated by spaces: ")
                user_numbers = list(map(int, user_input.split())) # Converting each input number to integer and creating a list
                if len(user_numbers) == self.difficulty:
                    return user_numbers
                else:
                    print(f"Please enter exactly {self.difficulty} numbers.")
            except ValueError:
                print("Invalid input. Please enter valid integers.")

    def is_list_equal(self, user_list):
        """Compares the generated sequence with the user's list."""
        return self.sequence == user_list

    def play(self):
        """Plays the memory game."""
        self.generate_sequence()
        user_list = self.get_list_from_user()
        if self.is_list_equal(user_list):
            print("Congratulations! You've remembered the numbers correctly.")
            return True
        print("Sorry, you didn't remember the numbers correctly.")
        return False


def memory_game(difficulty):
    return MemoryGame(difficulty).play()


if __name__ == "__main__":
    memory_game(int(input("Set the difficulty level (1-5): ")))