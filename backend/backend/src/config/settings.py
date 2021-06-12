import os
from . import local

# Secret key
SECRET_KEY = b"awubsyb872378t^*TG8y68&*&&*8y8yg9POB)*896ft7CR^56dfYUv"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_STR = "/api"

# DB
POSTGRES_USER = os.environ.get("POSTGRES_USER", local.POSTGRES_USER)
POSTGRES_PASS = os.environ.get("POSTGRES_PASS", local.POSTGRES_PASS)
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", local.POSTGRES_HOST)
POSTGRES_DB = os.environ.get("POSTGRES_DB", local.POSTGRES_DB)

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}/{POSTGRES_DB}"
)

# CORS
BACKEND_CORS_ORIGINS = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:8080",
]

ACCESS_TOKEN_EXPIRES_MINUTES = 60 * 24 * 8
