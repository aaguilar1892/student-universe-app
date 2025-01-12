from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, events, chat
from database import connect_db

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to MongoDB
connect_db()

# Include Routes
app.include_router(auth.router, prefix="/api/auth")
app.include_router(events.router, prefix="/api/events")
app.include_router(chat.router, prefix="/api/chat")

@app.get("/")
def root():
    return {"message": "Welcome to Student Universe API"}
