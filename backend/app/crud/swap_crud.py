# app/crud/swap_crud.py

from sqlalchemy.orm import Session
from app.models import Swap
from app.schemas import SwapCreate, SwapRead

def create_swap(db: Session, swap: SwapCreate) -> Swap:
    db_swap = Swap(
        initiator_id=swap.initiator_id,
        receiver_id=swap.receiver_id,
        item_offered_id=swap.item_offered_id,
        item_requested_id=swap.item_requested_id,
        status=swap.status
    )
    db.add(db_swap)
    db.commit()
    db.refresh(db_swap)
    return db_swap

def get_swap(db: Session, swap_id: int) -> Swap:
    return db.query(Swap).filter(Swap.id == swap_id).first()

def get_swaps(db: Session, skip: int = 0, limit: int = 10) -> list[Swap]:
    return db.query(Swap).offset(skip).limit(limit).all()

def update_swap(db: Session, swap_id: int, swap: SwapCreate) -> Swap:
    db_swap = get_swap(db, swap_id)
    if db_swap:
        db_swap.initiator_id = swap.initiator_id
        db_swap.receiver_id = swap.receiver_id
        db_swap.item_offered_id = swap.item_offered_id
        db_swap.item_requested_id = swap.item_requested_id
        db_swap.status = swap.status
        db.commit()
        db.refresh(db_swap)
    return db_swap

def delete_swap(db: Session, swap_id: int) -> None:
    db_swap = get_swap(db, swap_id)
    if db_swap:
        db.delete(db_swap)
        db.commit()
