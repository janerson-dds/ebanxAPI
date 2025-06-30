from fastapi import APIRouter, Response, HTTPException

router = APIRouter()

accounts = {}


@router.post("/reset")
def reset_state():
    accounts.clear()
    return Response(content="OK", media_type="text/plain", status_code=200)


@router.get("/balance")
def reset_state(account_id: str):
    if account_id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    return accounts[account_id]


@router.post("/event")
def reset_state():
    return Response(content="OK", media_type="text/plain", status_code=200)
