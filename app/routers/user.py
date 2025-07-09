from fastapi import APIRouter, HTTPException
from app.schemas.user import LoginRequest

router = APIRouter()

fake_user = {
    "email": "bhanu@gamil.com",
    "password": "123456"
}

@router.post("/login")
def login_user(data: LoginRequest):
    if data.email == fake_user["email"] and data.password == fake_user["password"]:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")