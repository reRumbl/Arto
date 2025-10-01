from typing import Any, TypeVar
from pydantic import BaseModel
from src.core.repository import BaseRepository

# --- Generic type (repository) ---
RepoT = TypeVar('RepoT', bound=BaseRepository)

# --- Generic types (pydantic schemas) ---
ReadSchemaT = TypeVar('ReadSchemaT', bound=BaseModel)
CreateSchemaT = TypeVar('CreateSchemaT', bound=BaseModel)
UpdateSchemaT = TypeVar('UpdateSchemaT', bound=BaseModel)


class BaseService[
    RepoT: BaseRepository, 
    ReadSchemaT: BaseModel, 
    CreateSchemaT: BaseModel, 
    UpdateSchemaT: BaseModel
]:
    
    def __init__(self, repository: RepoT, read_schema: type[ReadSchemaT]):
        self.repository = repository
        self.read_schema = read_schema

    async def create(self, schema: CreateSchemaT) -> ReadSchemaT:
        '''Create object'''
        
        instance_data = schema.model_dump()
        created_instance = await self.repository.create(**instance_data)
        
        return self.read_schema.model_validate(created_instance)

    async def get(self, pk: Any) -> ReadSchemaT | None:
        '''Get object'''
        
        instance = await self.repository.get(pk)
        
        if instance:
            return self.read_schema.model_validate(instance)
        
        return None

    async def update(self, pk: Any, schema: UpdateSchemaT) -> ReadSchemaT | None:
        '''Update object'''
        
        update_data = schema.model_dump(exclude_unset=True)
        updated_instance = await self.repository.update(pk, **update_data)
        
        if updated_instance:
            return self.read_schema.model_validate(updated_instance)
        
        return None

    async def delete(self, pk: Any) -> ReadSchemaT | None:
        '''Delete object'''
        
        deleted_instance = await self.repository.delete(pk)
        
        if deleted_instance:
            return self.read_schema.model_validate(deleted_instance)
        
        return None
