from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, HttpUrl


app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


# model field, nested model
class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="description", max_length=300)
    price: float | None = Field(
        gt=0, description="price")
    tax: float | None = None
    tags: set[str] = set()
    image: list[Image] | None = None


@app.put("/items/{items_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
