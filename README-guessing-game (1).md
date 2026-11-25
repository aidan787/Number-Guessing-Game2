# Number Guessing Game

A command-line number guessing game written in Python. The computer secretly picks a number between 1 and 100, and you try to guess it in as few attempts as possible.

## How it works

1. The game picks a random number from 1 to 100.
2. You type a guess.
3. The game tells you whether your guess was too high or too low, and shows your attempt count.
4. When you guess correctly, it tells you how many attempts it took and starts a new round with a new number.

## Run it

You need [Python 3](https://www.python.org/downloads/) installed. No other packages are required.

```bash
git clone https://github.com/aidan787/number-guessing-game.git
cd number-guessing-game
python GuessingGame.py
```

To quit, press `Ctrl+C`.

## Example

```
Please Enter Your Guess: 50
Your Score is 1
Your Guess Was Too Low!
Please Enter Your Guess: 75
Your Score is 2
Your Guess Was Too High!
Please Enter Your Guess: 63
Your Score is 3
You Have Guessed The Correct Number!
It took you 3 attempts.
Guess Another Number!
```

## What I practiced

- Using the `random` module to generate a number
- Nested `while` loops: an inner loop for each round and an outer loop to restart the game
- `if` / `elif` / `else` logic to compare the guess to the answer
- Keeping score with a counter and f-strings
