from pydantic import BaseModel, Field


class Event(BaseModel):
    type: str
    origin: str
    destination: str
    amount: int
