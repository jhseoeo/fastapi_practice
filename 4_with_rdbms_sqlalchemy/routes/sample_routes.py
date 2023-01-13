from fastapi import APIRouter
from services.sample_service import SampleService
from dto.sample_dto import SampleDTO


router = APIRouter(prefix="/sample")


@router.put("/", response_model=SampleDTO)
async def add_sample_data(sample: SampleDTO):
    return await SampleService.addSampleData(sample=sample)


@router.get("/{sample_id}", response_model=SampleDTO)
async def get_sample_data(sample_id: int):
    return await SampleService.getSampleData(sample_id=sample_id)


@router.post("/{sample_id}")
async def modify_sample_data(sample_id: int, sample: SampleDTO):
    return await SampleService.modifySampleData(sample_id=sample_id, sample=sample)


@router.delete("/{sample_id}")
async def delete_sample_data(sample_id: int):
    return await SampleService.deleteSampleData(sample_id=sample_id)
