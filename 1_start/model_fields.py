from typing import Union, List, Set
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, HttpUrl


app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    """
    ### nested model, using model field
    """

    name: str
    description: Union[str, None] = Field(
        default=None, title="description", max_length=300
    )
    price: Union[float, None] = Field(gt=0, description="price")
    tax: Union[float, None] = None
    tags: Set[str] = set()
    image: Union[List[Image], None] = None


@app.put("/items/{items_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    """
    ### a request body which uses model field
    """
    results = {"item_id": item_id, "item": item}
    return results
