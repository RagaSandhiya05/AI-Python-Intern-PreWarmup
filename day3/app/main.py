from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Intern Warm-up API",
    description="A beginner-friendly API built with FastAPI",
    version="1.0.0"
)


# Pydantic model for validating item data
class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)


# Sample in-memory data
items = {
    1: {"id": 1, "name": "Notebook", "price": 50.0},
    2: {"id": 2, "name": "Pen", "price": 10.0}
}

next_item_id = 3


# Endpoint 1: Health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Endpoint 2: Retrieve an item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return items[item_id]


# Endpoint 3: Create a new item
@app.post("/items", status_code=201)
def create_item(item: ItemCreate):
    global next_item_id

    new_item = {
        "id": next_item_id,
        "name": item.name,
        "price": item.price
    }

    items[next_item_id] = new_item
    next_item_id += 1

    return new_item
