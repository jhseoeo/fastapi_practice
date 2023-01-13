from pydantic import Field
from . import BaseDTO


class SampleDTO(BaseDTO):
    sampleId: int = Field(alias="sample_id")
    sampleDescription: str = Field(alias="sample_description")
