#!/usr/bin/env python3
"""Upload raw word data from API to the database. Not part of the main game."""

import pandas as pd

from word_guess.database import SessionLocal, bulk_copy_data_to_db
from word_guess.models import MasterWords1

URL = "https://random-words-api.kushcreates.com/api"

if __name__ == "__main__":
    df = pd.read_json(URL)
    print("read json:", len(df))
    df = df.drop_duplicates(subset=["word"])
    print("deduped:", len(df))
    # Ensure column names match the model (word, length, category, language; created_at is optional)
    records = df.to_dict(orient="records")
    print("starting copying the data")
    bulk_copy_data_to_db(records, MasterWords1)
    print("copy completed, querying the data now")
    db = SessionLocal()
    try:
        results = db.query(MasterWords1).all()
        print(f"Found {len(results)} records in the database")
    finally:
        db.close()
