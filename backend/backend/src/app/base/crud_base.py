from typing import List, Optional, Generic, TypeVar, Type

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ...db.base import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def exists(self, db: Session, **kwargs):
        return db.query(db.query(self.model.id).filter_by(**kwargs).exists()).scalar()

    def get_object_or_404(self, db: Session, id: int) -> Optional[ModelType]:
        pass

    def get(self, db: Session, **kwargs) -> Optional[ModelType]:
        return db.query(self.model).filter_by(**kwargs).first()

    def all(self, db: Session, *, skip=0, limit=100) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def filter(self, db: Session, **kwargs) -> List[ModelType]:
        return db.query(self.model).filter_by(**kwargs).all()

    def create(self, db: Session, *, schema: CreateSchemaType, **kwargs) -> ModelType:
        data = schema.dict()
        data.update(kwargs)

        db_obj = self.model(**data)

        try:
            db.add(db_obj)
        except:
            pass
        else:
            db.commit()
            db.refresh(db_obj)
        finally:
            return db_obj

    def update(
        self, db: Session, *, model: ModelType, schema: UpdateSchemaType
    ) -> ModelType:
        obj_data = jsonable_encoder(model)
        update_data = schema.dict(skip_defaults=True)
        for field in obj_data:
            if field in update_data:
                setattr(model, field, update_data[field])
        db.add(model)
        db.commit()
        db.refresh(model)
        return model

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
