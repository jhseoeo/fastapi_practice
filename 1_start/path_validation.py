from typing import Union
from fastapi import FastAPI, Query, Path

app = FastAPI()


@app.get("/items/a/{item_id}")
async def read_items(
    item_id: int = Path(title="ID of item to get"),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    """
    # adding metadata to path parameter
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/b/{item_id}")
async def read_items(
    item_id: int = Path(title="ID of item to get", ge=1),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    """
    ### item_id should be grater than or equal with given number
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/c/{item_id}")
async def read_items(
    item_id: int = Path(title="ID of item to get", ge=0, le=100),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    """
    ### suggest this condition of this route' path parameter
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
