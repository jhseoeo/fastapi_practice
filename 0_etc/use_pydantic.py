from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    userid: int
    name: str = "홍길동"
    signup: datetime | None = None
    friends: list[int] = []


# the data is casted to match User's declaration
external_data = {
    "userid": "123",
    "signup": "2023-01-01 12:00",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)
print(user)
print(user.friends)
