# app/crud/category_crud.py

from sqlalchemy.orm import Session
from app.models import Category
from app.schemas import CategoryCreate, CategoryRead

def create_category(db: Session, category: CategoryCreate) -> Category:
    db_category = Category(
        name=category.name,
        description=category.description
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_id: int) -> Category:
    return db.query(Category).filter(Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 10) -> list[Category]:
    return db.query(Category).offset(skip).limit(limit).all()

def update_category(db: Session, category_id: int, category: CategoryCreate) -> Category:
    db_category = get_category(db, category_id)
    if db_category:
        db_category.name = category.name
        db_category.description = category.description
        db.commit()
        db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int) -> None:
    db_category = get_category(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
