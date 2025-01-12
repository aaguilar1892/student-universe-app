from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List
from models import ChatMessage
from database import db
from datetime import datetime

router = APIRouter()

# List of connected clients
connected_clients: List[WebSocket] = []

# WebSocket endpoint for real-time chat
@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            message = ChatMessage(
                sender_email=data["sender_email"],
                receiver_email=data["receiver_email"],
                message=data["message"],
                timestamp=datetime.utcnow()
            )
            # Save message to MongoDB
            await db["chat_messages"].insert_one(message.dict(by_alias=True))
            
            # Broadcast message to all clients
            for client in connected_clients:
                await client.send_json(data)

    except WebSocketDisconnect:
        connected_clients.remove(websocket)
