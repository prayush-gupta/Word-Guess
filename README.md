# Word Guess

A word-guessing game where players guess a random word character-by-character, with optional AI-generated hints.

## Project structure

```
Word-Guess/
├── src/
│   └── word_guess/          # Main package
│       ├── __init__.py      # Version & public API
│       ├── __main__.py      # Entry point (python -m word_guess)
│       ├── config.py        # Settings from environment
│       ├── database.py      # Engine, session, persistence
│       ├── game_engine.py   # Game flow and round logic
│       ├── hint_generator.py
│       ├── user_interaction.py
│       ├── words_generator.py
│       └── models/
│           └── __init__.py  # SQLAlchemy models
├── scripts/                 # One-off tools (not part of the game)
│   ├── raw_data_upload_to_db.py
│   └── query_db.py
├── .env.example
├── pyproject.toml
└── README.md
```

## Setup

- **Python**: 3.11+
- Copy `.env.example` to `.env` and set `DATABASE_URL` (e.g. PostgreSQL).
- Install in editable mode: `pip install -e .` or `uv sync`, then run from the project root.

## Run the game

- From project root (with package installed):
  - `word-guess`
  - or `python -m word_guess`
- Ensure `DATABASE_URL` (and Google AI key for hints, if required) are set.

## Scripts

- **Upload words to DB**: `python scripts/raw_data_upload_to_db.py`
- **Query DB**: `python scripts/query_db.py`

Run scripts from the project root after installing the package so `word_guess` is importable.
