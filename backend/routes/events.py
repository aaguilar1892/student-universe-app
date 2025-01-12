from fastapi import APIRouter, HTTPException, Depends
from models import Event
from database import db
from middleware.auth_middleware import get_current_user
router = APIRouter()

@router.get("/")
async def get_events(user: str = Depends(get_current_user)):
    events = await db["events"].find().to_list(100)
    return events

@router.post("/")
async def create_event(event: Event):
    new_event = await db["events"].insert_one(event.dict(by_alias=True))
    return {"id": str(new_event.inserted_id)}
