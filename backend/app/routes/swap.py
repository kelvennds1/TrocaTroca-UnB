# app/routes/swap.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Swap
from app.schemas import SwapCreate, SwapRead
from app.database import get_db
from app.crud.swap_crud import create_swap, get_swap, get_swaps, update_swap, delete_swap

router = APIRouter()

@router.post(
    "/",
    response_model=SwapRead,
    summary="Criar novo swap",
    description="Cria um novo swap e retorna os detalhes do swap criado.",
    tags=["Swaps"],
)
def create_new_swap(swap: SwapCreate, db: Session = Depends(get_db)):
    return create_swap(db, swap)

@router.get(
    "/{swap_id}",
    response_model=SwapRead,
    summary="Obter um swap por ID",
    description="Retorna os detalhes do swap com o ID especificado.",
    tags=["Swaps"],
)
def read_swap(swap_id: int, db: Session = Depends(get_db)):
    swap = get_swap(db, swap_id)
    if swap is None:
        raise HTTPException(status_code=404, detail="Swap não encontrado")
    return swap

@router.get(
    "/",
    response_model=list[SwapRead],
    summary="Listar todos os swaps",
    description="Retorna uma lista de todos os swaps.",
    tags=["Swaps"],
)
def read_swaps(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_swaps(db, skip=skip, limit=limit)

@router.put(
    "/{swap_id}",
    response_model=SwapRead,
    summary="Atualizar um swap",
    description="Atualiza os detalhes do swap com o ID especificado.",
    tags=["Swaps"],
)
def update_existing_swap(swap_id: int, swap: SwapCreate, db: Session = Depends(get_db)):
    updated_swap = update_swap(db, swap_id, swap)
    if updated_swap is None:
        raise HTTPException(status_code=404, detail="Swap não encontrado")
    return updated_swap

@router.delete(
    "/{swap_id}",
    response_model=SwapRead,
    summary="Excluir um swap",
    description="Exclui o swap com o ID especificado.",
    tags=["Swaps"],
)
def delete_existing_swap(swap_id: int, db: Session = Depends(get_db)):
    delete_swap(db, swap_id)
    return {"detail": "Swap excluído com sucesso"}
