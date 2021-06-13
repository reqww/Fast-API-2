from sqlalchemy import Column, String, DateTime, Boolean, sql, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ...db.session import Base

# from ..base.model_base import BaseModel


class User(Base):
    __tablename__ = "users"

    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String(150))
    last_name = Column(String(150))
    date_join = Column(DateTime(timezone=True), server_default=sql.func.now())
    last_login = Column(DateTime)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=True)
    avatar = Column(String)


class SocialAccount(Base):
    __tablename__ = "social_account"

    account_id = Column(Integer)
    provider = Column(String)
    account_url = Column(String(150))
    account_login = Column(String(150))
    account_name = Column(String(150))

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", backref="social_account")
