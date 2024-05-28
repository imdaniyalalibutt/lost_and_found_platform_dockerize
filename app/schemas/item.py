from typing import Optional
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
    location: str
    status: str

class Item(BaseModel):
    id: int
    name: str
    description: str
    location: str
    status: str

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True
