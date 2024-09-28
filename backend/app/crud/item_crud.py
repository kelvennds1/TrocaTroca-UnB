# app/crud/item_crud.py

from sqlalchemy.orm import Session
from app.models import Item
from app.schemas import ItemCreate, ItemRead

def create_item(db: Session, item: ItemCreate) -> Item:
    db_item = Item(
        name=item.name,
        image=item.image,
        model=item.model,
        brand=item.brand,
        year_acquired=item.year_acquired,
        description=item.description,
        condition=item.condition,
        vaccines=item.vaccines,
        likes=item.likes,
        dislikes=item.dislikes,
        item_type=item.item_type,
        category_id=item.category_id,
        owner_id=item.owner_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int) -> Item:
    return db.query(Item).filter(Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 10) -> list[Item]:
    return db.query(Item).offset(skip).limit(limit).all()

def update_item(db: Session, item_id: int, item: ItemCreate) -> Item:
    db_item = get_item(db, item_id)
    if db_item:
        db_item.name = item.name
        db_item.image = item.image
        db_item.model = item.model
        db_item.brand = item.brand
        db_item.year_acquired = item.year_acquired
        db_item.description = item.description
        db_item.condition = item.condition
        db_item.vaccines = item.vaccines
        db_item.likes = item.likes
        db_item.dislikes = item.dislikes
        db_item.item_type = item.item_type
        db_item.category_id = item.category_id
        db_item.owner_id = item.owner_id
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int) -> None:
    db_item = get_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
