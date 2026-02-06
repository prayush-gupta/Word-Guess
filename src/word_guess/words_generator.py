"""Word selection from DB, APIs, or random-word service."""

import random
import requests

from word_guess.database import SessionLocal
from word_guess.models import MasterWords1
from sqlalchemy import func


def random_from_DB() -> str:
    """Pick a random English word from the master words table."""
    db = SessionLocal()
    try:
        row = (
            db.query(MasterWords1)
            .filter_by(language="en")
            .order_by(func.random())
            .first()
        )
        return row.word if row else "Generation Error"
    except Exception:
        return "Generation Error"
    finally:
        db.close()


def get_random_fruit_from_api() -> str:
    """Fetch a random fruit name from Fruityvice API."""
    response = requests.get("https://www.fruityvice.com/api/fruit/all")
    if response.status_code == 200:
        fruits_data = response.json()
        return random.choice(fruits_data)["name"]
    return "Failed to fetch fruits from API"


def get_random_words(count: int, diff: int | None = None, length: int | None = None) -> list[str] | str:
    """Fetch random words from herokuapp API. Returns list of words or error string."""
    url = f"https://random-word-api.herokuapp.com/word?number={count}"
    if length:
        url += f"&length={length}"
    if diff:
        url += f"&diff={diff}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return f"Error: {response.status_code}"


def word_generator(word_type: str) -> str:
    """Return a single word for the game based on user choice: d=DB, f=fruits, else=anything."""
    generation_try = 0
    keyword = "Generation Error"
    while generation_try < 3:
        if generation_try > 0:
            print("Retrying to generate a word, please wait...")
        try:
            if word_type == "d":
                keyword = random_from_DB().lower()
                break
            if word_type == "f":
                keyword = get_random_fruit_from_api().lower()
                break
            result = get_random_words(1, diff=2, length=random.randrange(6, 15))
            if isinstance(result, str) and result.startswith("Error:"):
                generation_try += 1
                continue
            keyword = result[0].lower()
            break
        except Exception:
            generation_try += 1
    return keyword if generation_try < 3 else "Generation Error"
