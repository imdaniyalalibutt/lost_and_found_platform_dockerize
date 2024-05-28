from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.db.fake_users import get_hardcoded_user

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login/")
async def login(login_data: LoginRequest):
    user = get_hardcoded_user()  # No need to await as it's not a coroutine now
    if user.username == login_data.username and user.verify_password(login_data.password):
        return {"msg": "Login successful"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
