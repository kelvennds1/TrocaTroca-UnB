# app/routes/item.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Item
from app.schemas import ItemCreate, ItemRead
from app.database import get_db
from app.crud.item_crud import create_item, get_item, get_items, update_item, delete_item

router = APIRouter()

@router.post(
    "/",
    response_model=ItemRead,
    summary="Criar novo item",
    description="Cria um novo item e retorna os detalhes do item criado.",
    tags=["Itens"],
)
def create_new_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)

@router.get(
    "/{item_id}",
    response_model=ItemRead,
    summary="Obter um item por ID",
    description="Retorna os detalhes do item com o ID especificado.",
    tags=["Itens"],
)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

@router.get(
    "/",
    response_model=list[ItemRead],
    summary="Listar todos os itens",
    description="Retorna uma lista de todos os itens.",
    tags=["Itens"],
)
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_items(db, skip=skip, limit=limit)

@router.put(
    "/{item_id}",
    response_model=ItemRead,
    summary="Atualizar um item",
    description="Atualiza os detalhes do item com o ID especificado.",
    tags=["Itens"],
)
def update_existing_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    updated_item = update_item(db, item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return updated_item

@router.delete(
    "/{item_id}",
    response_model=ItemRead,
    summary="Excluir um item",
    description="Exclui o item com o ID especificado.",
    tags=["Itens"],
)
def delete_existing_item(item_id: int, db: Session = Depends(get_db)):
    delete_item(db, item_id)
    return {"detail": "Item excluído com sucesso"}
