from functools import wraps
from fastapi import HTTPException
from src.core.exceptions import InternalServerErrorException


def default_router_exceptions(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerErrorException()
    return wrapper
