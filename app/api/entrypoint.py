from fastapi import APIRouter

from app.api.endpoints.account import account

api_router = APIRouter()

api_router.include_router(account.router)
