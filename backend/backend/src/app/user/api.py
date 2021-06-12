from fastapi import APIRouter, Depends

from ..auth.permissions import get_user

from . import models, schemas


user_router = APIRouter()


@user_router.get("/me", response_model=schemas.UserPublic)
def user_me(current_user: models.User = Depends(get_user)):
    if current_user:
        return current_user
