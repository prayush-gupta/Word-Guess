import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = os.environ.get("DATABASE_URL")

# Handle the case where the URL starts with 'postgres://' (common in Replit/Heroku)
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class GameResult(Base):
    __tablename__ = "game_results"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    keyword = Column(String)
    result = Column(String)
    points = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)

def save_game_result(category, keyword, result, points):
    db = SessionLocal()
    try:
        db_result = GameResult(
            category=category,
            keyword=keyword,
            result=result,
            points=points
        )
        db.add(db_result)
        db.commit()
    finally:
        db.close()
