from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.exceptions import NotFoundException
from app.db.database import get_db
from app.services import user_service
from app.schemas import user as user_schema

router = APIRouter()

@router.post("/", response_model=user_schema.UserRead)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get("/", response_model=list[user_schema.UserRead])
def read_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

@router.get("/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise NotFoundException("User not found")
    return {"id": user_id, "name": "John"}
