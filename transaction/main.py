from fastapi import FastAPI
from routes.transaction import transaction_router

app = FastAPI()

# Include transaction routes
app.include_router(transaction_router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Transaction API"}