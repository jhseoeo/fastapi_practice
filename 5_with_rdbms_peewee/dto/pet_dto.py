from pydantic import Field
from . import BaseDTO


class PetDTO(BaseDTO):
    petId: str = Field(alias="pet_id")
    groupId: str = Field(alias="group_id")
    someFields: int = Field(alias="some_fields")
