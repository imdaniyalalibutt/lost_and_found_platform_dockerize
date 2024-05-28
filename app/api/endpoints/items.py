from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.item import ItemCreate, Item
from app.db.models import Item as ItemModel
from app.db.base import get_db  # Corrected import
from app.db.crud import update_item
from app.schemas.item import ItemUpdate
from app.db.crud import delete_item



router = APIRouter()

@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = ItemModel(name=item.name, description=item.description, location=item.location, status=item.status)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = db.query(ItemModel).offset(skip).limit(limit).all()
    return items

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@router.put("/items/{item_id}")
async def update_item_by_id(
    item_id: int, item_update: ItemUpdate, db: Session = Depends(get_db)
):
    """
    Update an item by ID.
    """
    db_item = update_item(db, item_id, item_update)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/items/{item_id}")
async def delete_item_by_id(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item by ID.
    """
    deleted = delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
