from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Swap
from app.schemas import SwapCreate, SwapRead
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=SwapRead)
def create_swap(swap: SwapCreate, db: Session = Depends(get_db)):
    db_swap = Swap(**swap.dict())
    db.add(db_swap)
    db.commit()
    db.refresh(db_swap)
    return db_swap

@router.get("/{swap_id}", response_model=SwapRead)
def read_swap(swap_id: int, db: Session = Depends(get_db)):
    swap = db.query(Swap).filter(Swap.id == swap_id).first()
    if swap is None:
        raise HTTPException(status_code=404, detail="Swap not found")
    return swap

@router.put("/{swap_id}", response_model=SwapRead)
def update_swap(swap_id: int, swap: SwapCreate, db: Session = Depends(get_db)):
    db_swap = db.query(Swap).filter(Swap.id == swap_id).first()
    if db_swap is None:
        raise HTTPException(status_code=404, detail="Swap not found")
    
    for key, value in swap.dict().items():
        setattr(db_swap, key, value)
    
    db.commit()
    db.refresh(db_swap)
    return db_swap

@router.delete("/{swap_id}", response_model=SwapRead)
def delete_swap(swap_id: int, db: Session = Depends(get_db)):
    swap = db.query(Swap).filter(Swap.id == swap_id).first()
    if swap is None:
        raise HTTPException(status_code=404, detail="Swap not found")
    
    db.delete(swap)
    db.commit()
    return swap
