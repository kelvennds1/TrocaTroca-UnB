from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserLogin, Token
from app.auth import create_access_token, verify_password

router = APIRouter()

@router.post("/login", response_model=Token)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_login.email).first()
    if not user or not verify_password(user_login.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
