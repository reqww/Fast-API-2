from fastapi import HTTPException

from ..user.schemas import UserCreate
from . import crud, schemas
from ..base.utils.generate import generate_password


def create_social_account(db, profile: schemas.SocialAccount):
    if crud.social_account.exists(db, **profile.dict()):
        raise HTTPException(400, detail="social acc exists.")

    if crud.user.exists(db, username=profile.account_login):
        user = crud.user.get(db, username=profile.account_login)
    else:
        new_user = UserCreate(
            username=profile.account_login,
            email=f"sos{profile.account_id}@gmail.com",
            password=generate_password(),
            first_name=profile.account_name.split()[0],
        )

        user = crud.user.create(db, schema=new_user)

    acc = crud.social_account.create(db, schema=profile, user_id=user.id)

    return acc
