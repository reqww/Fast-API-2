from fastapi import APIRouter
from .auth.api import auth_router

api_router = APIRouter()

# api_router.include_router(blog_router, prefix="/blog", tags=["blog"])
api_router.include_router(auth_router, tags=["login"])