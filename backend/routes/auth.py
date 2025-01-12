from fastapi import APIRouter, HTTPException, Depends
from models import User
from database import db
from services.auth_service import hash_password, verify_password, create_access_token

router = APIRouter()

# User Registration
@router.post("/register")
async def register_user(user: User):
    existing_user = await db["users"].find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    user.password = hash_password(user.password)
    new_user = await db["users"].insert_one(user.dict(by_alias=True))
    return {"id": str(new_user.inserted_id)}

# User Login
@router.post("/login")
async def login_user(email: str, password: str):
    user = await db["users"].find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": user["email"]})
    return {"access_token": token, "token_type": "bearer"}
