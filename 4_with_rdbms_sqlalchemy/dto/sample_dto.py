from pydantic import BaseModel, Field


class SampleDTO(BaseModel):
    # sampleId: int
    # sampleDescription: str
    sampleId: int = Field(alias="sample_id")
    sampleDescription: str = Field(alias="sample_description")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
