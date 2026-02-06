"""Database engine, session, and persistence helpers."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from word_guess.config import get_database_url
from word_guess.models import Base, GameResult, MasterWords1

DATABASE_URL = get_database_url()
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")

# engine = create_engine(DATABASE_URL)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Create all tables in the database."""
    Base.metadata.create_all(bind=engine)


def save_game_result(
    user_name: str,
    category: str,
    keyword: str,
    result: str,
    points: int,
    hint_used: str,
    max_guesses: int,
    incorrect_guesses: int,
) -> None:
    """Persist a single game result."""
    db = SessionLocal()
    try:
        db.add(
            GameResult(
                user_name=user_name,
                category=category,
                keyword=keyword,
                result=result,
                points=points,
                hint_used=hint_used,
                max_guesses=max_guesses,
                incorrect_guesses=incorrect_guesses,
            )
        )
        db.commit()
    finally:
        db.close()


def bulk_copy_data_to_db(records: list[dict], model_class: type) -> None:
    """Bulk insert records using the given model class (e.g. MasterWords1)."""
    db = SessionLocal()
    try:
        db.bulk_insert_mappings(model_class, records)
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
