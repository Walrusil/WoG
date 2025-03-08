import os
import random

from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


class ScoreManager:
    def __init__(self):
        # Ensure the scores file exists
        if not os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'w') as f:
                try:
                    f.write('0')  # Initialize with 0 points
                except IOError as e:
                    print(f"ERROR: Cannot initialize the score file! [{e}]")

    def read_score(self):
        """Read the score from the score file"""
        try:
            with open(SCORES_FILE_NAME, 'r') as f:
                return f.read()
        except (FileNotFoundError, IOError) as e:
            print(f"ERROR: Cannot read from score file! [{e}]")
        return BAD_RETURN_CODE

    def get_score(self):
        """Read the score from tghe score file, checks validity and returns a valid value"""
        score = self.read_score().strip()
        try:
            score = int(score)
        except ValueError as e:
            print(f"ERROR: Score ({score}) is not an integer! [{e}]")
            return 0

        if score < 0:
            print(f"ERROR: Score ({score}) is negative!")
            return 0

        return score

    def calculate_winning_score(self, difficulty):
        """Calculate the score for the difficulty"""
        return 3*difficulty + 5

    def write_score(self, score):
        """Write the score to the score file"""
        try:
            with open(SCORES_FILE_NAME, 'w') as f:
                f.write(str(score))
        except IOError as e:
            print(f"ERROR: Cannot save the score ({score})! [{e}]")
            return BAD_RETURN_CODE

    def add_score(self, difficulty):
        """Calculate the new score, update the score file and return the new score"""
        score = self.get_score() + self.calculate_winning_score(difficulty)
        self.write_score(score)
        return score


if __name__ == "__main__":
    score_manager = ScoreManager()

    original_score = score_manager.get_score()
    print("Original score:   ", original_score)
    random_difficulty = random.randint(1, 5)  # Example difficulty level
    print("Random difficulty:", random_difficulty)
    winning_score = score_manager.calculate_winning_score(random_difficulty)
    print("Winning score:    ", winning_score)
    new_score = original_score + winning_score
    print("New score:        ", new_score)
    score_manager.write_score(new_score)
    # score_manager.add_score(random_difficulty)