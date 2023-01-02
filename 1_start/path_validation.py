from fastapi import FastAPI, Query, Path

app = FastAPI()


# adding metadata to path parameter
@app.get("/items/a/{item_id}")
async def read_items(
    item_id: int = Path(title="ID of item to get"),
    q: str | None = Query(default=None, alias="item-query")
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# item_id should be grater than or equal with given number
@app.get("/items/b/{item_id}")
async def read_items(
    item_id: int = Path(title="ID of item to get", ge=1),
    q: str | None = Query(default=None, alias="item-query")
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/c/{item_id}")
async def read_items(
    item_id: int = Path(title="ID of item to get", ge=0, le=100),
    q: str | None = Query(default=None, alias="item-query")
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
