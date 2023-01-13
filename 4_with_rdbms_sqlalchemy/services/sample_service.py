from models.sample import Sample
from dto.sample_dto import SampleDTO
from orm.sample_orm import SampleORM


class SampleService:
    @staticmethod
    async def addSampleData(sample: SampleDTO):
        return await SampleORM.add_sample(sample=Sample(**sample.dict(by_alias=True)))

    @staticmethod
    async def getSampleData(sample_id: int):
        sample = await SampleORM.find_by_sample_id(sample_id=sample_id)

        if sample is None:
            return SampleDTO(sampleId=-99, sampleDescription="데이터없어요")
        else:
            return sample

    @staticmethod
    async def modifySampleData(sample_id: int, sample: SampleDTO):
        return await SampleORM.modify_sample(
            sample_id=sample_id, sample=Sample(**sample.dict(by_alias=True))
        )

    @staticmethod
    async def deleteSampleData(sample_id: int):
        return await SampleORM.delete_sample(sample_id=sample_id)
