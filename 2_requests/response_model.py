from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """
    ### declares output(response) model
    """
    return item


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/user/1", response_model=UserIn)
async def create_user(user: UserIn):
    """
    ### respond same model with request
    """
    return user


@app.post("/user/2", response_model=UserOut)
async def create_user(user: UserIn):
    """
    ### respond modified model with request
    """
    return user


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_none=True)
async def read_item(item_id: str):
    """
    ### if response_model_exclude_unset == True, excludes fields when its value is None(null)
    ### try also response_model_exclude_none, response_model_exclude_defaults
    """
    return items[item_id]


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    """
    ### always include given fields
    """
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    """
    ### always exclude given field
    """
    return items[item_id]
