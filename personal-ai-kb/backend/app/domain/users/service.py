from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.users.repository import UserRepository
from app.core.security import hash_password, verify_password, create_token
from app.core.exceptions import ConflictException, UnauthorizedException

class UserService:
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def register(self, email: str, password: str, full_name: str | None = None) -> dict:
        existing = await self.repo.get_by_email(email)
        if existing:
            raise ConflictException("Email already registered")

        hashed = hash_password(password)
        user = await self.repo.create(email=email, hashed_pw=hashed, full_name=full_name)

        return {
            "access_token": create_token(str(user.id), "access"),
            "refresh_token": create_token(str(user.id), "refresh"),
            "token_type": "bearer",
        }

    async def login(self, email: str, password: str) -> dict:
        user = await self.repo.get_by_email(email)
        if not user or not verify_password(password, user.hashed_pw):
            raise UnauthorizedException("Invalid email or password")

        return {
            "access_token": create_token(str(user.id), "access"),
            "refresh_token": create_token(str(user.id), "refresh"),
            "token_type": "bearer",
        }