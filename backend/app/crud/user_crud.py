# app/crud/user_crud.py

from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate, UserRead
from fastapi import HTTPException

from app.auth import hash_password

def create_user(db: Session, user: UserCreate) -> User:
    # Verificação de email único
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = hash_password(user.password_hash)
    db_user = User(
        registration=user.registration,
        password_hash=hashed_password,
        name=user.name,
        user_name=user.user_name,
        email=user.email,
        profile_picture=user.profile_picture
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_users(db: Session, skip: int = 0, limit: int = 10) -> list[User]:
    return db.query(User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user: UserCreate) -> User:
    db_user = get_user(db, user_id)
    
    # Verificar se o email já está em uso por outro usuário
    if db.query(User).filter(User.email == user.email).first() and db_user.email != user.email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
  
    db_user.registration = user.registration
    if user.password_hash:  # Verifica se a senha foi fornecida para atualização
        db_user.password_hash = hash_password(user.password_hash)  # Hash da nova senha
    db_user.name = user.name
    db_user.user_name = user.user_name
    db_user.email = user.email
    db_user.profile_picture = user.profile_picture
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int) -> None:
    db_user = get_user(db, user_id)
    db.delete(db_user)
    db.commit()
