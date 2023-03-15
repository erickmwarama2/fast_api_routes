from typing import List
from pydantic import BaseModel

class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item

    class Config:
        schema_extra = {
            "Example": {
                "id": 1,
                "item": {
                    "item": "this is the example item",
                    "status": "this is the example status"
                }
            }
        }

class TodoItem(BaseModel):
    item: Item
    class Config:
        schema_extra = {
            "example": {
                "item": {
                    "item": "Read the next chapter of the book",
                    "status": "This is the status"
                }
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]
    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": {
                            "item": "Example schema 1",
                            "status": "Example status 1"
                        }
                    },
                    {
                        "item": {
                            "item": "Example schema 2",
                            "status": "Example status 2"
                        }
                    }
                ]
            }
        }