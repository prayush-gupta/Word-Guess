"""SQLAlchemy models for word_guess."""

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class GameResult(Base):
    """Stores the result of a single game."""

    __tablename__ = "game_results"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    category = Column(String)
    keyword = Column(String)
    result = Column(String)
    points = Column(Integer)
    hint_used = Column(String)
    max_guesses = Column(Integer)
    incorrect_guesses = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)


class MasterWords1(Base):
    """Master list of words from the API source."""

    __tablename__ = "master_words_kushcreates"

    word = Column(String, primary_key=True, index=True)
    length = Column(Integer)
    category = Column(String)
    language = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
