# WoG - World of Games

This repository includes the World of Games project for the DevOps course

## Folder Structure

```
WorldOfGames/
├── CurrencyRouletteGame.py
├── Docker-compose.yaml 
├── Dockerfile 
├── GuessGame.py
├── Jenkinsfile
├── Live.py
├── MainGame.py
├── MainScores.py
├── MemoryGame.py
├── README.md
├── requirements.txt
├── Score.py
├── Scores.txt
├── Utils.py
└── tests/
    └── e2e.py
```

## Usage
1. Run ***MainGame*** to select one of three games
   - A **memory** game
   - A **guessing** game
   - A **currency roulette** game
2. You can access http://localhost:5000/score to see your score

## Jenkins Workflows

Trigger: On every push to the `main` branch.
Actions:
1. Check out the repository
2. Build the docker image
3. Run tha WoG application with the score service exposed on localhost port 8777 
4. Run a unit test that checks the validity of the score (Should be between 1 and 1000)
5. Push the docker image to Docker Hub if the test passed successfully