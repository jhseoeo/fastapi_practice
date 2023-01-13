from models.sample import Sample
from dto.sample_dto import SampleDTO
from orm import postgresql
from orm.sample_orm import SampleORM


class SampleService:
    @staticmethod
    @postgresql().atomic()
    async def addSampleData(sample_request: SampleDTO):
        sample = Sample(
            sample_id=sample_request.sampleId,
            sample_description=sample_request.sampleDescription,
        )
        await SampleORM.save(sample)
        return sample

    @staticmethod
    async def getSampleData(sample_id: str):
        return await SampleORM.find_by_sample_id(sample_id=sample_id)

    @staticmethod
    @postgresql().atomic()
    async def modifySampleData(sample_id: str, sample_request: SampleDTO):
        sample = await SampleORM.find_by_sample_id(sample_id=sample_id)

        sample.sample_id = sample_request.sampleId
        sample.sample_description = sample_request.sampleDescription
        await SampleORM.save(sample)

        return sample

    @staticmethod
    @postgresql().atomic()
    async def deleteSampleData(sample_id: str):
        await SampleORM.delete_by_id(sample_id=sample_id)
