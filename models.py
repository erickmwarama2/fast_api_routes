from typing import List, Optional
from pydantic import BaseModel
from fastapi import Form

class Item(BaseModel):
    item: str
    status: Optional[str]

class Todo(BaseModel):
    id: Optional[int]
    item: Item

    @classmethod
    def as_form(cls, item: str = Form(...)):
        print(f"{item}")
        item_obj = Item(item=item)
        return cls(item=item_obj)

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