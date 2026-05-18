import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.users.models import User

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, user_id: str) -> User | None:
        result = await self.db.execute(select(User).where(User.id == uuid.UUID(user_id)))
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def create(self, email: str, hashed_pw: str, full_name: str | None = None) -> User:
        user = User(email=email, hashed_pw=hashed_pw, full_name=full_name)
        self.db.add(user)
        await self.db.flush()
        return user