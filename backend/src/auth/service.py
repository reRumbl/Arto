from datetime import datetime
from src.core.service import BaseService
from src.auth.repository import AuthRepository
from src.auth.schemas import User, UserRegister, UserLogin, UserUpdate, TokenPairResponse
from src.auth.utils.passwords import get_password_hash, verify_password
from src.auth.utils.tokens import create_token_pair, decode_access_token, refresh_token_state
from src.auth.constants import JTI, EXP
from src.core.exceptions import BadRequestException, NotFoundException


class AuthService(BaseService[AuthRepository, User, UserRegister, UserUpdate]):
    
    async def register(self, data: UserRegister) -> User:
        user = await self.repository.get_by_email(data.email)
        if user:
            raise BadRequestException('User already registered')
        
        user_data = data.model_dump(exclude={'confirm_password'})
        user_data['hashed_password'] = get_password_hash(user_data['password'].get_secret_value())
        user_data.pop('password', None)
        
        user = await self.repository.create(**user_data)
        user_schema = User.model_validate(user)
        
        return user_schema
    
    async def login(self, data: UserLogin) -> TokenPairResponse:
        user = await self.repository.get_by_email(data.email)
        
        if not user or not verify_password(data.password.get_secret_value(), user.hashed_password):
            raise NotFoundException('Wrong email or password')
        
        user = User.model_validate(user)
        token_pair = create_token_pair(user)
        
        return TokenPairResponse(
            access_token=token_pair.access.token,
            refresh_token=token_pair.refresh.token
        )
        
    async def logout(self, token: str) -> None:
        payload = await decode_access_token(self.repository, token)
        await self.repository.create_black_list_token(
            id=payload[JTI], 
            expire=datetime.fromtimestamp(payload[EXP])
        )
    
    async def refresh(self, token: str) -> TokenPairResponse:
        new_access_token = await refresh_token_state(token)
        return TokenPairResponse(
            access_token=new_access_token,
            refresh_token=token
        )
    
    async def get_by_username(self, username: str) -> User:
        user = await self.repository.get_by_username(username)
        
        if not user:
            raise NotFoundException('User not found')
        
        user_schema = User.model_validate(user)
        
        return user_schema
