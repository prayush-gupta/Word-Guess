#!/usr/bin/env python3
"""Query game results and master words from the database."""

from word_guess.database import SessionLocal
from word_guess.models import GameResult, MasterWords1

if __name__ == "__main__":
    db = SessionLocal()
    try:
        game_count = db.query(GameResult).count()
        print(f"Found {game_count} games in the database")
        word_count = db.query(MasterWords1).count()
        print(f"Found {word_count} random words in the database")
    finally:
        db.close()
