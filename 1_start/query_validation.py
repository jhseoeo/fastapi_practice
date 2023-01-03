from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()


# q should meet min_length, max_length, regex
@app.get("/items/a")
async def read_items(
    q: str | None = Query(default=None, min_length=3, max_length=50, regex="([A-Z])")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# q is now required
@app.get("/items/b")
async def read_items(
    q: str | None = Query(default=..., min_length=3, max_length=50, regex="([A-Z])")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# same with above
# ... is replaced by Required
@app.get("/items/b")
async def read_items(
    q: str
    | None = Query(default=Required, min_length=3, max_length=50, regex="([A-Z])")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# list of query parameter
# /items/list?q=asd&q=asd
@app.get("/items/list")
async def read_items(q: list[str] | None = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items


# adding query parameter's metadata
@app.get("/items/more")
async def read_items(
    q: list[str]
    | None = Query(
        default=["foo", "bar"], title="query string", description="this is querystring"
    )
):
    query_items = {"q": q}
    return query_items


# alias
@app.get("/items/alias")
async def read_items(q: str | None = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# deprecating
@app.get("/items/depreciated")
async def read_items(
    q: str | None = Query(default=None, alias="item-query", deprecated=True)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
