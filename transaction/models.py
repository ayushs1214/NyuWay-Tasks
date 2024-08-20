from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

class Transaction(BaseModel):
    user_id: str
    amount: float
    type: Literal['credit', 'debit']
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    description: str = None