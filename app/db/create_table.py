# In a file like app/db/create_tables.py
from app.db.base import Base
from app.db.sessions import engine

# Import all your SQLAlchemy models here so that they are registered with Base
from app.db.models import User

def create_tables():
    Base.metadata.create_all(bind=engine)

# Call the function to create the tables when your application starts
create_tables()
