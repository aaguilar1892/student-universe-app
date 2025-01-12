from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

class User(BaseModel):
    id: Optional[ObjectId] = Field(alias="_id")
    email: str
    password: str
    name: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Event(BaseModel):
    id: Optional[ObjectId] = Field(alias="_id")
    title: str
    description: str
    date: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
