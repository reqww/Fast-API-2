from fastapi import APIRouter, Depends

from ..auth.permissions import get_user

from . import models, schemas, service


user_router = APIRouter()


@user_router.get("/me", response_model=schemas.UserPublic)
def user_me(current_user: models.User = Depends(get_user)):
    if current_user:
        return current_user


@user_router.post("/test/create", response_model=schemas.User_G_Pydantic)
async def test_create(user: schemas.UserCreateInRegistration):
    return await service.user_objects.create(user)
