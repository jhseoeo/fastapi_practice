from typing import Union
from fastapi import FastAPI, Body
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class Item_(BaseModel):
    """
    ### model with example data
    """

    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


@app.put("/items/ex1/{item_id}")
async def update_item(item_id: int, item: Item_):
    """
    ### body with model example
    """
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items/ex2/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(
        example={
            "name": "Foo",
            "description": "a very nice item",
            "price": 35.4,
            "tax": 3.2,
        }
    ),
):
    """
    ### body with parameter example
    """
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items/ex3/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(
        examples={
            "normal": {
                "summary": "normal data",
                "value": {
                    "name": "Foo",
                    "description": "a very nice item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "converted data",
                "description": "FastAPI convert price strings to actual numbers",
                "value": {"name": "Bar", "price": "35.4"},
            },
            "invalid": {
                "summary": "Invalid data",
                "value": {"name": "Baz", "price": "thirty five point four"},
            },
        }
    ),
):
    """
    # body with multiple parameter examples
    """
    results = {"item_id": item_id, "item": item}
    return results
