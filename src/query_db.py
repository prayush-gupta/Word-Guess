from database import SessionLocal, GameResult

def fetch_all_results():
    # Create a new session
    db = SessionLocal()
    try:
        # Query all results from the game_results table
        results = db.query(GameResult).all()
        
        print(f"Found {len(results)} games in the database:\n")
        for res in results:
            print(f"Date: {res.created_at} | Category: {res.category} | Word: {res.keyword} | Result: {res.result} | Points: {res.points}")
            
    finally:
        # Always close the session
        db.close()

if __name__ == "__main__":
    fetch_all_results()
