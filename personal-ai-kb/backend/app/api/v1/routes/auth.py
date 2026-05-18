from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.ext.asyncio import AsyncConnection
from app.core.database import get_db
from app.core.security import decode_token, create_token
from app.domain.users.service import UserService
from app.domain.users.repository import UserRepository
from app.domain.users.models import User
from app.api.v1.dependencies import get_current_user

router = APIRouter(prefix="/auth",tags = ["auth"])

class RegisterRequest(BaseModel):
    email : EmailStr
    password = str
    full_name  = str | None = None

class LoginRequest(BaseModel):
    email = EmailStr
    password = str

class RefreshRequest(BaseModel):
    refresh_token = str

@router.post("/register",status_code=201)
async def register(payload : RegisterRequest , db : AsyncConnection = Depends(get_db)):
    service = UserService(db)
    return await service.register(payload.email,payload.password,payload.full_name)

@router.post("/login")
async def login(payload:LoginRequest, db: AsyncConnection = Depends(get_db)):
    service = UserService(db)
    return await service.login(payload.email,payload.password)

@router.post("/refresh")
async def refresh(payload:RefreshRequest):
    try:
        decoded = decode_token(payload.refresh_token)

    except ValueError:
        from fastapi import HTTPException,status
        raise HTTPException (status_code=status.HTTP_401_UNAUTHORIZED,detail= "Invalid refresh token")
    
    if decoded.get("type")!="refresh":
        from fastapi import HTTPException,status
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "Wrong token type")
    
    new_access_token = create_token(decoded["sub"],"access")
    return {"access_token" : new_access_token,"token_type" :"bearer"}

@router.get("/me")
async def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": str(current_user.id),
        "email": current_user.email,
        "full_name": current_user.full_name,
        "plan": current_user.plan,
    }