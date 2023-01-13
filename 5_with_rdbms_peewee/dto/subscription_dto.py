from pydantic import Field
from . import BaseDTO


class SubscriptionDTO(BaseDTO):
    groupId: str = Field(alias="group_id")
    someData: bool = Field(alias="some_data")
