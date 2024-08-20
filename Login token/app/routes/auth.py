from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.database import get_user, create_user
from app.security import verify_password, create_access_token

router = APIRouter()

@router.post("/register")
async def register(username: str, password: str):
    user = await get_user(username)
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    await create_user(username, password)
    return {"message": "User created successfully"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user(form_data.username)
    if not user or not verify_password(form_data.password, user['hashed_password']):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user['username']})
    return {"access_token": access_token, "token_type": "bearer"}