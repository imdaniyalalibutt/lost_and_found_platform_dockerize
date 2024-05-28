from sqlalchemy.orm import Session
from . import models
from app.schemas.item import ItemCreate, ItemUpdate


def create_item(db: Session, item: ItemCreate):
    """Create a new item in the database."""
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item(db: Session, item_id: int):
    """Retrieve an item from the database by its ID."""
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of items from the database."""
    return db.query(models.Item).offset(skip).limit(limit).all()


def update_item(db: Session, item_id: int, item_update: ItemUpdate):
    """Update an existing item in the database."""
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    for field, value in item_update.dict().items():
        setattr(db_item, field, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    """Delete an item from the database."""
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    db.delete(db_item)
    db.commit()
