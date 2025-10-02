from sqlalchemy import select
from src.core.repository import BaseRepository
from src.auth.models import UserModel, BlackListTokenModel
from src.auth.schemas import BlackListTokenCreate


class AuthRepository(BaseRepository[UserModel]):
    
    async def get_by_email(self, email: str) -> UserModel | None:
        query = select(UserModel).where(UserModel.email == email)
        result = await self.session.execute(query)
        user_db = result.scalars().first()
        return user_db

    async def get_by_username(self, username: str) -> UserModel | None:
        query = select(UserModel).where(UserModel.username == username)
        result = await self.session.execute(query)
        user_db = result.scalars().first()
        return user_db

    async def create_black_list_token(self, data: BlackListTokenCreate) -> None:
        black_listed = BlackListTokenModel(**data.model_dump())
        self.session.add(black_listed)
        await self.session.commit()
    