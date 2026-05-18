from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.ext.asyncio import AsyncConnection
from app.core.database import get_db
from app.core.security import decode_token, create_token
from app.domain.users.service import UserService
from app.domain.users.repository import UserRepository
from app.domain.users.models import User
from app.api.v1.dependencies import get_current_user

