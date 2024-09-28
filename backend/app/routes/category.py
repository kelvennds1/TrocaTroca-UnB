# app/routes/category.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Category
from app.schemas import CategoryCreate, CategoryRead
from app.database import get_db
from app.crud.category_crud import create_category, get_category, get_categories, update_category, delete_category

router = APIRouter()

@router.post(
    "/",
    response_model=CategoryRead,
    summary="Criar nova categoria",
    description="Cria uma nova categoria e retorna os detalhes da categoria criada.",
    tags=["Categorias"],
)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)

@router.get(
    "/{category_id}",
    response_model=CategoryRead,
    summary="Obter uma categoria por ID",
    description="Retorna os detalhes da categoria com o ID especificado.",
    tags=["Categorias"],
)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = get_category(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return category

@router.get(
    "/",
    response_model=list[CategoryRead],
    summary="Listar todas as categorias",
    description="Retorna uma lista de todas as categorias.",
    tags=["Categorias"],
)
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_categories(db, skip=skip, limit=limit)

@router.put(
    "/{category_id}",
    response_model=CategoryRead,
    summary="Atualizar uma categoria",
    description="Atualiza os detalhes da categoria com o ID especificado.",
    tags=["Categorias"],
)
def update_existing_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    updated_category = update_category(db, category_id, category)
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return updated_category

@router.delete(
    "/{category_id}",
    response_model=CategoryRead,
    summary="Excluir uma categoria",
    description="Exclui a categoria com o ID especificado.",
    tags=["Categorias"],
)
def delete_existing_category(category_id: int, db: Session = Depends(get_db)):
    category = delete_category(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return {"detail": "Categoria excluída com sucesso"}
