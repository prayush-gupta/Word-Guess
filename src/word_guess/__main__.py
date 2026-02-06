"""Run the game when the package is executed with python -m word_guess."""

from word_guess import game_start
from scripts.raw_data_upload_to_db import data_loader


def main() -> None:
    data_loader()
    game_start()

if __name__ == "__main__":
    main()
