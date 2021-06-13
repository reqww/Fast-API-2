from .settings import DATABASE_URL

TORTOISE_ORM = {
    "connections": {"default": "postgres://postgres:pass@127.0.0.1:5432/postgres"},
    "apps": {
        "models": {
            "models": ["src.app.user.models", "src.app.auth.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
