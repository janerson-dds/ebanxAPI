from typing import Union

from fastapi import APIRouter, Response, HTTPException
from app.api.dto.event import Event
from app.api.service.account.account_service import AccountService

router = APIRouter()

accounts: dict[str, int] = {}

service = AccountService()

@router.post("/reset")
def reset():
    service.reset_state()
    return Response(content="OK", media_type="text/plain", status_code=200)


@router.get("/balance")
def balance(account_id: str):
    amount = service.get_balance(account_id)

    if amount != "0":
        return Response(content=amount, media_type="text/plain", status_code=200)
    else:
        return Response(content="0", media_type="text/plain", status_code=404)


@router.post("/event", status_code=201)
def event(event: Event):
    output = service.handle_event(event)

    if output:
        return output
    else:
        return Response(content="0", media_type="text/plain", status_code=404)
