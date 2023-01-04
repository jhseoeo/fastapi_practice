from typing import Union, List, Dict
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI()


# a superclass that inherits its attribute
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int


items1 = {
    "item1": {"description": "난 차였어", "type": "car"},
    "item2": {"description": "난 이제 비행기야", "type": "plane", "size": 5},
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    """
    ### multiple response models
    """
    return items1[item_id]


class Item(BaseModel):
    name: str
    description: str


items2 = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Bar", "description": "my aeroplane"},
]


@app.get("/items/", response_model=List[Item])
async def read_items():
    """
    ### list of models
    """
    return items2


@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}
