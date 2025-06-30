from typing import Union

from fastapi import APIRouter, Response, HTTPException
from app.api.dto.event import Event
router = APIRouter()

accounts: dict[str, int] = {}


@router.post("/reset")
def reset_state():
    accounts.clear()
    return Response(content="OK", media_type="text/plain", status_code=200)


@router.get("/balance")
def get_balance(account_id: str):
    if account_id in accounts:
        return Response(content=str(accounts[account_id]), media_type="text/plain", status_code=200)
    else:
        return Response(content="0", media_type="text/plain", status_code=404)


@router.post("/event")
def handle_event(event: Event):
    match event.type:
        case 'deposit':
            return Response(content="OK", media_type="text/plain", status_code=200)
        case 'withdraw':
            return Response(content="OK", media_type="text/plain", status_code=200)
        case 'transfer':
            return Response(content="OK", media_type="text/plain", status_code=200)
