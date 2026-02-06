"""Main game flow and round logic."""

import os
import sys

import pandas as pd

from word_guess.database import init_db, save_game_result
from word_guess.hint_generator import ask_for_hint
from word_guess.user_interaction import user_interaction
from word_guess.words_generator import word_generator


def game_start() -> None:
    """Initialize DB, greet user, and start the game loop."""
    init_db()
    print("Welcome to the Word Guessing Game!")
    user_name = user_interaction("What is your name? ")
    max_guesses = max(
        5,
        user_interaction("How many guesses would you like to have? ", "int", 0),
    )
    game_controller(max_guesses, user_name)


def game_controller(max_guesses: int, user_name: str) -> None:
    """Run the outer loop: word type, word generation, play round, save, repeat."""
    play = "yes"
    i = 0
    won = 0
    overall_result: list[list] = []

    while play == "yes":
        i += 1
        os.system("clear")

        word_type = user_interaction(
            "What kind of words would you like to guess? [Local DB[d]/Anything[a]/Fruits[f]] "
        )
        os.system("clear")

        print("Generating a word, please wait...")
        keyword = word_generator(word_type)

        if keyword == "Generation Error":
            os.system("clear")
            print("Sorry, there was an error generating a word. Please try again later.")
            if len(overall_result) > 0:
                break
            sys.exit(1)

        local_won, hint_used, incorrect_guesses = play_the_game(keyword, max_guesses)
        won += local_won

        category = "DB" if word_type == "d" else "Fruit" if word_type == "f" else "Anything"
        result_label = "Correct" if local_won == 1 else "Wrong"
        save_game_result(
            user_name,
            category,
            keyword.upper(),
            result_label,
            local_won,
            hint_used,
            max_guesses,
            incorrect_guesses,
        )

        overall_result.append([
            category,
            keyword.upper(),
            result_label,
            hint_used,
            local_won,
        ])
        print()
        print("You have won", won, "out of", i, "games")
        print()
        play = user_interaction("Would you like to play again? (yes/no) ").lower()

    print()
    print()
    final_result = pd.DataFrame(
        overall_result,
        columns=["Category", "Keyword", "Result", "Hint", "Points"],
    )
    final_result["Total Score"] = final_result["Points"].cumsum()
    print(final_result)


def play_the_game(keyword: str, total_guess: int) -> tuple[int, str, int]:
    """Run one round. Returns (1 if won else 0, hint_used, incorrect_guesses)."""
    underscores = "_" * len(keyword)
    hint_requested = "no"
    guess_counter = 0
    result = ""
    hint = ""

    os.system("clear")
    print(underscores)
    print()
    print("You are allowed ", total_guess, " incorrect guesses")
    print()
    print("Press ~ for a hint")
    print()

    while guess_counter < total_guess and underscores != keyword:
        print()
        guess = user_interaction("Enter a letter: ", "string", 1)

        if guess == "~":
            os.system("clear")
            try:
                hint = ask_for_hint(keyword)
                hint_requested = "yes"
            except Exception:
                hint = "Sorry, no hint available. Please try again later"
        elif guess in keyword:
            replacement_counter = 0
            while replacement_counter < len(keyword):
                if keyword[replacement_counter] == guess:
                    underscores = (
                        underscores[:replacement_counter]
                        + guess
                        + underscores[replacement_counter + 1 :]
                    )
                replacement_counter += 1
            result = "You guessed a letter correctly"
        else:
            result = "Wrong guess!"
            guess_counter += 1

        os.system("clear")
        print(underscores)
        print()
        print(result)
        print()
        print("You have ", total_guess - guess_counter, " remaining guesses")
        if hint_requested == "yes":
            print()
            print("HINT: ", hint)

    if underscores == keyword:
        print()
        print()
        print("CONGRATS!! You guessed the word", keyword.upper(), "correctly")
        return 1, hint_requested, guess_counter
    print()
    print()
    print("Sorry, you lost!!")
    print("The word was ", keyword.upper())
    return 0, hint_requested, guess_counter
