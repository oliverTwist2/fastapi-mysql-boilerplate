from fastapi import APIRouter, HTTPException, Depends
from datetime import timedelta
from sqlalchemy.orm import Session

from app.auth import schemas, jwt, utils
from app.db.database import get_db
from app.db import models
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES

router = APIRouter()

@router.post("/login", response_model=schemas.Token)
def login(user: schemas.UserAuth, db: Session = Depends(get_db)):
    try:
        db_user = db.query(models.User).filter(models.User.email == user.email).first()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database query failed: {e}")

    if not db_user or not utils.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect credentials")
    
    access_token = jwt.create_token(
        {"sub": str(db_user.id)},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    refresh_token = jwt.create_token(
        {"sub": str(db_user.id)},
        expires_delta=timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    )

    return {"access_token": access_token, "refresh_token": refresh_token}

@router.post("/refresh", response_model=schemas.Token, include_in_schema=False)
def refresh_token(refresh_token: str):
    try:
        payload = jwt.decode_token(refresh_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid or expired refresh token: {e}")

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Malformed token")

    new_access_token = jwt.create_token(
        {"sub": user_id},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    new_refresh_token = jwt.create_token(
        {"sub": user_id},
        expires_delta=timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token
    }

