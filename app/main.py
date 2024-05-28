from fastapi import FastAPI
from app.api.endpoints.auth import router as auth_router
from app.api.endpoints.items import router as items_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(items_router, prefix="/items")
