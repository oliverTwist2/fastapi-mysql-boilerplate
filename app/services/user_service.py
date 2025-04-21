from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db import models
from app.schemas import user as user_schema
from app.auth import utils
from fastapi import HTTPException

def create_user(db: Session, user: user_schema.UserCreate):
    try:
        db_user = models.User(name=user.name, email=user.email, hashed_password=utils.hash_password(user.password))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to create user: {e}")

def get_users(db: Session):
    try:
        return db.query(models.User).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve users: {e}")
