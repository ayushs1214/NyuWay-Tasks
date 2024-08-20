from motor.motor_asyncio import AsyncIOMotorClient
from app.models import UserModel
from app.security import get_password_hash

client = AsyncIOMotorClient("mongodb://localhost:27017")
database = client["nyuway"]
user_collection = database["users"]

async def create_user(username: str, password: str):
    hashed_password = get_password_hash(password)
    user = UserModel(username=username, hashed_password=hashed_password)
    await user_collection.insert_one(user.dict())

async def get_user(username: str):
    user = await user_collection.find_one({"username": username})
    return user