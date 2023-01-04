from typing import List, Union
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    userid: int
    name: str = "홍길동"
    signup: Union[datetime, None] = None
    friends: List[int] = []


# the data is casted to match User's declaration
external_data = {
    "userid": "123",
    "signup": "2023-01-01 12:00",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)
print(user)
print(user.friends)
