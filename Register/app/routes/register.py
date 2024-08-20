from fastapi import APIRouter
from app.models.user import User
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

router = APIRouter()

MONGO_DETAILS = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_DETAILS)
db = client["nyuway"]
register_collection = db["register"]

@router.post("/register")
async def register_user(user: User):
    unique_id = str(ObjectId())
    
    user_data = user.dict()
    user_data["_id"] = unique_id
    await register_collection.insert_one(user_data)
    
    return {"message": "User registered successfully"}