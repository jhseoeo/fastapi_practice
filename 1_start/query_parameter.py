from fastapi import FastAPI, Query

app = FastAPI()


# Query parameters
@app.get("/items/")
async def read_items(a: int = 0, b: int = 10):
    return {"sum": a + b}


# Optional Query parameter
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    else:
        return {"item_id": item_id}


# Type casting of Query Parameter
@app.get("/items/types/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "awesome!"})
    return item


# Types of Query Parameter
# needy : required
# skip : skippable(optional)
# limit : skippable, may not be exist
@app.get("/items/needy/{item_id}")
async def reqd_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item_id = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item_id
