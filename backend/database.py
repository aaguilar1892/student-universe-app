from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI")
client = None
db = None

def connect_db():
    global client, db
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.get_database("student_universe")
