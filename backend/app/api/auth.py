from fastapi import APIRouter
from app.core.security import create_token

router = APIRouter()

@router.post("/login")
def login(email: str):
    token = create_token({"sub": email})
    return {"access_token": token}
