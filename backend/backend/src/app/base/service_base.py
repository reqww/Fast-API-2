from pydantic import BaseModel
from typing import TypeVar, Generic, Type, Optional

from tortoise import Model


ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)


class BaseService:
    model: Type[ModelType]
    create_schema: Type[CreateSchemaType]
    update_schema: Type[UpdateSchemaType]
    get_schema: Type[GetSchemaType]

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(
        self, schema: CreateSchemaType, *args, **kwargs
    ) -> Optional[GetSchemaType]:
        obj = await self.model.create(**schema.dict(exclude_unset=True), **kwargs)
        return await self.get_schema.from_tortoise_orm(obj)

    async def update(
        self, schema: UpdateSchemaType, *args, **kwargs
    ) -> Optional[GetSchemaType]:
        pass

    async def get(self):
        pass

    async def delete(self):
        pass
