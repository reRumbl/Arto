from typing import Any, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import Base

T = TypeVar('T', bound=Base)


class BaseRepository[T]:
    
    def __init__(self, model: type[T], session: AsyncSession):
        self.model = model
        self.session = session
    
    async def create(self, **kwargs: Any) -> T:
        '''Create model instance with provided kwargs'''
        
        instance = self.model(**kwargs)
        
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        
        return instance
    
    async def get(self, pk: Any) -> T | None:
        '''Get model instance by primary key'''
        
        instance = await self.session.get(self.model, pk)
        return instance
    
    async def update(self, pk: Any, **kwargs: Any) -> T | None:
        '''Update model instance with provided kwargs by primary key'''
        
        instance = await self.session.get(self.model, pk)
        
        if instance is None:
            return None
        
        for key, value in kwargs.items():
            setattr(instance, key, value)
            
        await self.session.commit()
        await self.session.refresh(instance)
        
        return instance
    
    async def delete(self, pk: Any) -> bool:
        '''Delete model instance by primary key'''
        
        instance = await self.session.get(self.model, pk)
        
        if instance is None:
            return False
        
        await self.session.delete(instance)
        await self.session.commit()
        
        return True
        