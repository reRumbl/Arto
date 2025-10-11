from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from src.auth.repository import AuthRepository
from src.auth.service import AuthService
from src.auth.models import UserModel
from src.auth.schemas import User
from src.auth.utils.tokens import decode_access_token
from src.auth.constants import SUB
from src.core.dependencies import SessionDep
from src.core.exceptions import UnauthorizedException


def get_auth_repository(session: SessionDep) -> AuthRepository:
    return AuthRepository(UserModel, session)


AuthRepositoryDep = Annotated[AuthRepository, Depends(get_auth_repository)]


def get_auth_service(repository: AuthRepositoryDep) -> AuthService:
    return AuthService(repository, User)


AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')
TokenDep = Annotated[str, Depends(oauth2_scheme)]


async def get_current_user(token: TokenDep, repository: AuthRepositoryDep) -> User:
    payload = await decode_access_token(repository, token)
    user = await repository.get(payload[SUB])
    
    if not user:
        raise UnauthorizedException()
    
    user_schema = User.model_validate(user)
    return user_schema


CurrentUserDep = Annotated[User, Depends(get_current_user)]
