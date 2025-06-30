from typing import Optional

from pydantic import BaseModel, Field


class Event(BaseModel):
    type: str
    origin: Optional[str] = None
    destination: Optional[str] = None
    amount: int
