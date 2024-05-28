# app/api/services/user.py

from sqlalchemy.orm import Session
from app.db.models import User
from app.api.models.user import UserCreate

def create_user(db: Session, user_data: UserCreate):
    db_user = User(username=user_data.username, email=user_data.email)
    db_user.set_password(user_data.password)  # Use set_password method
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
