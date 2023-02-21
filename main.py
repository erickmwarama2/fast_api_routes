from fastapi import FastAPI, APIRouter
from todo import todo_router

app = FastAPI()
router = APIRouter()

@app.get('/')
async def welcome() -> dict:
    return {"message":"Welcome to FastAPI"}

@router.get('/hello')
async def say_hello() -> dict:
    return {"message": "Hello Mr. Erick"}

app.include_router(todo_router)