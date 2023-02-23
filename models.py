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