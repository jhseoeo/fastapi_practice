from datetime import datetime
from typing import List
from pydantic import Field
from . import BaseDTO


class Log(BaseDTO):
    anyContent: str


class UserDTO(BaseDTO):
    userId: str = Field(alias="user_id")
    phoneNumber: str = Field(alias="phone_number")
    anyInteger: int = Field(alias="any_integer")
    registeredDate: datetime = Field(alias="registered_date")
    recentLog: Log = Field(alias="recent_log")
