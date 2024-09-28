# app/routes/user.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate, UserRead
from app.database import get_db
from app.crud.user_crud import create_user, get_user, update_user, delete_user

router = APIRouter()

@router.post(
    "/",
    response_model=UserRead,
    summary="Criar novo usuário",
    description="Cria um novo usuário e retorna os detalhes do usuário criado.",
    tags=["Usuários"],
)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get(
    "/{user_id}",
    response_model=UserRead,
    summary="Obter um usuário por ID",
    description="Retorna os detalhes do usuário com o ID especificado.",
    tags=["Usuários"],
)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)

@router.put(
    "/{user_id}",
    response_model=UserRead,
    summary="Atualizar um usuário",
    description="Atualiza os detalhes do usuário com o ID especificado.",
    tags=["Usuários"],
)
def update_existing_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user)

@router.delete(
    "/{user_id}",
    response_model=UserRead,
    summary="Excluir um usuário",
    description="Exclui o usuário com o ID especificado.",
    tags=["Usuários"],
)
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    delete_user(db, user_id)
    return {"detail": "Usuário excluído com sucesso"}
