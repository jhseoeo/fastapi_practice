from models.sample import Sample


class SampleORM:
    @staticmethod
    async def find_by_sample_id(sample_id: int) -> Sample:
        return Sample.get_or_none(Sample.sample_id == sample_id)

    @staticmethod
    async def save(sample: Sample):
        if await SampleORM.find_by_sample_id(sample.sample_id) is not None:
            sample.save()
        else:
            sample.save(force_insert=True)

    @staticmethod
    async def delete(sample: Sample):
        sample.delete_instance()

    @staticmethod
    async def delete_by_id(sample_id: int) -> Sample:
        query = Sample.delete().where(Sample.sample_id == sample_id)
        query.execute()
