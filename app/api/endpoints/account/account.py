from fastapi import APIRouter, Response

router = APIRouter()


@router.post("/reset")
def reset_state():
    return Response(content="OK", media_type="text/plain", status_code=200)


@router.get("/balance")
def reset_state():
    return Response(content="OK", media_type="text/plain", status_code=200)


@router.post("/event")
def reset_state():
    return Response(content="OK", media_type="text/plain", status_code=200)
