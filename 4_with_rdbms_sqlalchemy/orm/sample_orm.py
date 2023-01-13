from models.sample import Sample
from . import postgresql


class SampleORM:
    @staticmethod
    async def find_by_sample_id(sample_id: int) -> Sample:
        return postgresql().query(Sample).filter(Sample.sample_id == sample_id).first()

    @staticmethod
    async def add_sample(sample: Sample) -> Sample:
        row = sample
        postgresql().add(row)
        postgresql().commit()
        return row

    @staticmethod
    async def modify_sample(sample_id: int, sample: Sample) -> Sample:
        row = (
            postgresql()
            .query(Sample)
            .filter(Sample.sample_id == sample_id)
            .update(
                {
                    "sample_id": sample.sample_id,
                    "sample_description": sample.sample_description,
                }
            )
        )
        postgresql().commit()
        return row

    @staticmethod
    async def delete_sample(sample_id: int) -> Sample:
        postgresql().query(Sample).filter(Sample.sample_id == sample_id).delete()
        postgresql().commit()
