from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional
from datetime import datetime

# Pydantic requires a custom encoder for MongoDB ObjectId
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

# User Model
class User(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr
    password: str
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "student@example.com",
                "password": "password123",
                "name": "John Doe"
            }
        }

# Event Model
class Event(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    title: str
    description: str
    date: datetime
    created_by: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "AI Workshop",
                "description": "An engaging AI workshop for beginners.",
                "date": "2024-06-20T15:30:00",
                "created_by": "student@example.com"
            }
        }

# Chat Message Model
class ChatMessage(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    sender_email: EmailStr
    receiver_email: EmailStr
    message: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "sender_email": "student1@example.com",
                "receiver_email": "student2@example.com",
                "message": "Hey, are you coming to the hackathon?"
            }
        }
