from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Required

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(default=Required),
    item: Item = Body(default=Required, embed=True),
    user: User = Body(default=Required, embed=True),
    importance: int = Body(default=Required, gt=0),
    q: str | None = Query(default=None)
):
    results = {"item_id": item_id, "item": item,
               "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
