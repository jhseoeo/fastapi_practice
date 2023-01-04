from typing import Union, List
from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()


@app.get("/items/a")
async def read_items(
    q: Union[str, None] = Query(
        default=None, min_length=3, max_length=50, regex="([A-Z])"
    )
):
    """
    ### q should meet min_length, max_length, regex
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/b")
async def read_items(
    q: Union[str, None] = Query(
        default=..., min_length=3, max_length=50, regex="([A-Z])"
    )
):
    """
    ### q is now required
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/b")
async def read_items(
    q: Union[str, None] = Query(
        default=Required, min_length=3, max_length=50, regex="([A-Z])"
    )
):
    """
    ### same with above. (...) is replaced by Required
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/list")
async def read_items(q: Union[List[str], None] = Query(default=["foo", "bar"])):
    """
    ### list of query parameter ex) /items/list?q=asd&q=asd
    """
    query_items = {"q": q}
    return query_items


@app.get("/items/more")
async def read_items(
    q: Union[List[str], None] = Query(
        default=["foo", "bar"], title="query string", description="this is querystring"
    )
):
    """
    ### adding query parameter's metadata
    """
    query_items = {"q": q}
    return query_items


@app.get("/items/alias")
async def read_items(q: Union[str, None] = Query(default=None, alias="item-query")):
    """
    ### alias
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/depreciated")
async def read_items(
    q: Union[str, None] = Query(default=None, alias="item-query", deprecated=True)
):
    """
    ### deprecating
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
