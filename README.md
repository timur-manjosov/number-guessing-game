# number-guessing-game

A small command-line game where the player guesses a randomly chosen
number between 1 and 10, with hints after each guess.

## Features

- Generates a random number from 1 to 10
- Tells the player whether their guess is too low or too high
- Handles invalid input gracefully by catching a `ValueError`
- Lets the player play multiple rounds in a row

## How to run

This project requires Python 3.

First, create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Then run the game:

```bash
python main.py
```

## What I learned

- How to guard against non-integer input using try / except
- That a `while True` loop can be exited with `break`
- How to organize code into functions and reuse them
- That reading the input once at the start of the loop is enough
