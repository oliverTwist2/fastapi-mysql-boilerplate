from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Add this function to provide a database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        raise RuntimeError(f"Database session error: {e}")
    finally:
        db.close()
