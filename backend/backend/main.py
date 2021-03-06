from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from tortoise.contrib.fastapi import register_tortoise

from src.config import settings
# from src.db.session import SessionLocal
from src.app import routers

app = FastAPI(
    title="FASTAPI2",
    description="Author - REQWW",
    version="0.1.0",
)


app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
# app.include_router(routers.api_router, prefix=settings.API_V1_STR)

register_tortoise(
    app,
    db_url=settings.DATABASE_URL,
    modules={"models": settings.APPS_MODELS},
    generate_schemas=False,
    add_exception_handlers=True,
)


# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()

#     return response


app.include_router(routers.api_router, prefix=settings.API_STR)
