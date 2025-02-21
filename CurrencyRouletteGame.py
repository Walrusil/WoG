import random
import requests


class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.exchange_rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        """Fetches the current exchange rate from USD to ILS."""
        try:
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            data = response.json()
            return data['rates']['ILS']
        except Exception as e:
            print("Error fetching exchange rate:", e)
            return None

    def get_money_interval(self, total_value):
        """Generates an interval based on the exchange rate and difficulty."""
        if self.exchange_rate is None:
            return None
        margin = 5 - self.difficulty
        lower_bound = total_value * self.exchange_rate - margin
        upper_bound = total_value * self.exchange_rate + margin
        return lower_bound, upper_bound, total_value * self.exchange_rate

    def get_guess_from_user(self):
        """Prompts the user to guess the value in ILS."""
        while True:
            try:
                guess = float(input("Guess the value in ILS: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play(self):
        """Plays the currency roulette game."""
        dollars = random.randint(1, 100) # Generate a random number between 1 and 100
        interval = self.get_money_interval(dollars)
        if interval is None:
            print("Could not retrieve exchange rate. Game cannot be played.")
            return False

        lower_bound, upper_bound, correct_value = interval

        print(f"The current exchange rate from Dollar to ILS is {self.exchange_rate}.")
        print(f"You have ${dollars} in your account. How much does it worth in ILS?")
        # print(f"(The value is somewhere between {lower_bound:.2f} and {upper_bound:.2f})") # This print in only for debugging!

        user_guess = self.get_guess_from_user()
        if lower_bound <= user_guess <= upper_bound:
            print("Congratulations! Your guess was within the correct range.")
            return True
        else:
            print(f"Sorry, the correct value was {correct_value:.2f} ILS.")
            return False


def currency_roulette(difficulty):
    return CurrencyRouletteGame(difficulty).play()


if __name__ == "__main__":
    currency_roulette(int(input("Set the difficulty level (1-5): ")))