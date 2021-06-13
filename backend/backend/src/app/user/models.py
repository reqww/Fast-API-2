from sqlalchemy import Column, String, DateTime, Boolean, sql, Integer, ForeignKey
from sqlalchemy.orm import relationship

from tortoise import models, fields


class User(models.Model):

    username = fields.CharField(max_length=100, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=100)
    first_name = fields.CharField(max_length=100, null=True)
    last_name = fields.CharField(max_length=100, null=True)
    date_join = fields.DatetimeField(auto_now_add=True)
    last_login = fields.DatetimeField(null=True)
    is_active = fields.BooleanField(default=True)
    is_staff = fields.BooleanField(default=True)
    is_superuser = fields.BooleanField(default=True)
    avatar = fields.CharField(max_length=100, null=True)

    class Meta:
        table = "user_user"


class SocialAccount(models.Model):

    account_id = fields.IntField()
    provider = fields.CharField(max_length=100)
    account_url = fields.CharField(max_length=200)
    account_login = fields.CharField(max_length=100)
    account_name = fields.CharField(max_length=100)

    user = fields.ForeignKeyField(
        "models.User", related_name="social", on_delete=fields.CASCADE
    )

    class Meta:
        table = "user_social_account"
