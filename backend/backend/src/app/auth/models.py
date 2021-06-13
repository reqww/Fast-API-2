from tortoise import models, fields


class Verification(models.Model):
    """Модель для подтверждения регистрации пользователя"""

    link = fields.UUIDField()
    user = fields.ForeignKeyField(
        "models.User", related_name="verif", on_delete=fields.CASCADE
    )

    class Meta:
        table = "auth_verification"
