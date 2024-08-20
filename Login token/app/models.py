from pydantic import BaseModel, Field, ConfigDict
from bson import ObjectId
from typing import Optional

class UserModel(BaseModel):
    id: Optional[ObjectId] = Field(alias='_id')
    username: str
    hashed_password: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
        }