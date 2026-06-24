"""A small, polished terminal number-guessing game.

The player tries to guess a secret number within a fixed range. After every
guess the game responds with a hint, and once the number is found the player
can choose to play again.
"""

import random

# --- Configuration ---------------------------------------------------------

LOWER_BOUND = 1
UPPER_BOUND = 10

# --- Visual helpers --------------------------------------------------------

WIDTH = 44


def divider(char: str = "─") -> str:
    """Return a horizontal divider line spanning the interface width."""
    return char * WIDTH


def banner() -> None:
    """Print the game's title banner."""
    print()
    print(f"╭{'─' * WIDTH}╮")
    print(f"│{'🎯  NUMBER  GUESSING  GAME  🎯':^{WIDTH}}│")
    print(f"╰{'─' * WIDTH}╯")
    print(f"  Guess my secret number between "
          f"{LOWER_BOUND} and {UPPER_BOUND}.")
    print()


# --- Input handling --------------------------------------------------------

def ask_guess() -> int:
    """Prompt until the player enters a valid integer, then return it."""
    while True:
        raw = input("  Your guess ➜ ").strip()
        try:
            return int(raw)
        except ValueError:
            print("  ⚠️  Please enter a whole number.\n")


def ask_play_again() -> bool:
    """Ask whether to start another round. Return True to keep playing."""
    answer = input("  Play again? [Y/n] ➜ ").strip().lower()
    return answer not in {"n", "no"}


# --- Game logic ------------------------------------------------------------

def play_round() -> None:
    """Play a single round until the secret number is guessed correctly."""
    secret = random.randint(LOWER_BOUND, UPPER_BOUND)
    attempts = 0

    while True:
        guess = ask_guess()
        attempts += 1

        if guess < LOWER_BOUND or guess > UPPER_BOUND:
            print(f"  🤔 Out of range — pick {LOWER_BOUND} to "
                  f"{UPPER_BOUND}.\n")
        elif guess < secret:
            print("  ⬆️  Too low!\n")
        elif guess > secret:
            print("  ⬇️  Too high!\n")
        else:
            tries = "try" if attempts == 1 else "tries"
            print()
            print(divider())
            print(f"  🎉 Correct! You won in {attempts} {tries}.")
            print(divider())
            print()
            return


def main() -> None:
    """Run the banner, the game loop, and the goodbye message."""
    banner()
    while True:
        play_round()
        if not ask_play_again():
            break
        print()

    print("\n  👋 Thanks for playing!\n")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n  👋 Goodbye!\n")
