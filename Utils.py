import os
import platform

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def screen_cleaner():
    """Clears the screen"""
    if platform.system() == "Windows":
        os.system('cls')  # Clear screen for Windows
    else:
        os.system('clear')  # Clear screen for Unix/Linux/Mac


if __name__ == "__main__":
    input("Press Enter to clear the screen...")
    screen_cleaner()
    print("Screen cleared!")