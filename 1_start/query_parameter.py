from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(a: int = 0, b: int = 10):
    """
    ### Query parameters
    """
    return {"sum": a + b}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    """
    ### Optional Query parameter
    """
    if q:
        return {"item_id": item_id, "q": q}
    else:
        return {"item_id": item_id}


@app.get("/items/types/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    """
    ### Type casting of Query Parameter
    """
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "awesome!"})
    return item


# needy : required
# skip : skippable(optional)
# limit : skippable, may not be exist
@app.get("/items/needy/{item_id}")
async def reqd_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    """
    ### Types of Query Parameter
    """
    item_id = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item_id
