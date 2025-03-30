from Live import *
from MemoryGame import memory_game
from GuessGame import guess_game
from CurrencyRouletteGame import currency_roulette
from Score import ScoreManager
from MainScores import ScoreServer
import time

games = {1: memory_game,
         2: guess_game,
         3: currency_roulette}

print("Loading the score server...")
score_server = ScoreServer()
time.sleep(1)

name = get_name()
print(welcome(name))

while True:
    load_game()
    game = select_game()
    if game == 4:
        print(f"\nBye {name}. See you next time...")
        score_server.stop()
        exit(0)
    difficulty = select_difficulty()
    print("")
    if games[game](difficulty):  # Game won
        ScoreManager().add_score(difficulty)