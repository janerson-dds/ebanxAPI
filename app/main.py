from fastapi import FastAPI

from app.api.entrypoint import api_router

app = FastAPI(title="EBANX API")

app.include_router(api_router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "API iniciada com sucesso!"}
