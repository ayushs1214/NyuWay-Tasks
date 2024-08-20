from fastapi import APIRouter, HTTPException, status
from models import Transaction
from database import transaction_collection
from bson import ObjectId

transaction_router = APIRouter()

@transaction_router.post("/transaction", status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction: Transaction):
    if transaction.type == 'debit' and transaction.amount <= 0:
        raise HTTPException(status_code=400, detail="Debit amount must be positive")
    if transaction.type == 'credit' and transaction.amount <= 0:
        raise HTTPException(status_code=400, detail="Credit amount must be positive")

    transaction_dict = transaction.dict()
    result = await transaction_collection.insert_one(transaction_dict)
    transaction_id = result.inserted_id

    return {"transaction_id": str(transaction_id), "status": "Transaction recorded successfully"}

@transaction_router.get("/transactions/{user_id}")
async def get_transactions(user_id: str):
    transactions = await transaction_collection.find({"user_id": user_id}).to_list(length=100)
    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found for this user")
    
    # Convert ObjectId to string
    for transaction in transactions:
        transaction["_id"] = str(transaction["_id"])
    
    return transactions