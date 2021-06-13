import os
from . import local

# Secret key
SECRET_KEY = os.environ.get("SECRET_KEY", local.SECRET_KEY)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_STR = "/api"

PROJECT_NAME = "Proj"

# DB
POSTGRES_USER = os.environ.get("POSTGRES_USER", local.POSTGRES_USER)
POSTGRES_PASS = os.environ.get("POSTGRES_PASS", local.POSTGRES_PASS)
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", local.POSTGRES_HOST)
POSTGRES_DB = os.environ.get("POSTGRES_DB", local.POSTGRES_DB)

ALCH_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}/{POSTGRES_DB}"
)

DATABASE_URL = (
    f"postgres://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}/{POSTGRES_DB}"
)

# CORS
BACKEND_CORS_ORIGINS = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:8080",
]

APPS_MODELS = [
    "src.app.user.models",
    "src.app.auth.models",
    "aerich.models",
]

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8
