from typing import Optional
from sqlalchemy.orm import Session
from ..auth.security import verify_password, get_password_hash
from ..base.crud_base import CRUDBase

from .models import User, SocialAccount
from . import schemas


class UserCRUD(CRUDBase[User, schemas.UserCreate, schemas.UserUpdate]):
    """CRUD for user"""

    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def get_by_username_email(
        self, db: Session, *, username: str, email: str
    ) -> Optional[User]:
        return (db.query(User).filter(User.username == username).first()) or (
            db.query(User).filter(User.email == email).first()
        )

    def create(self, db: Session, *, schema: schemas.UserCreate) -> User:
        db_obj = User(
            username=schema.username,
            email=schema.email,
            password=get_password_hash(schema.password),
            first_name=schema.first_name,
        )

            
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

    def create_superuser(self, db: Session, *, schema: schemas.UserCreate) -> User:
        db_obj = User(
            username=schema.username,
            email=schema.email,
            password=get_password_hash(schema.password),
            first_name=schema.first_name,
            is_active=schema.is_active,
            is_superuser=schema.is_superuser,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(
        self, db: Session, *, username: str, password: str
    ) -> Optional[User]:
        user = self.get_by_username(db, username=username)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser

    def update_password(self, db: Session, user: User, hashed_password: str):
        user.password = hashed_password
        db.add(user)
        db.commit()


user = UserCRUD(User)


class SocialCRUD(CRUDBase[SocialAccount, schemas.SocialAccount, schemas.SocialAccount]):
    """CRUD for SocialAccount"""


social_account = SocialCRUD(SocialAccount)
