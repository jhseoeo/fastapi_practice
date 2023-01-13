from models.pet import Pet


class PetORM:
    @staticmethod
    async def find_by_pet_id(pet_id: str) -> Pet:
        return Pet.get_or_none(Pet.pet_id == pet_id)

    @staticmethod
    async def save(pet: Pet):
        if await PetORM.find_by_pet_id(pet.pet_id) is not None:
            pet.save()
        else:
            pet.save(force_insert=True)

    @staticmethod
    async def delete(pet: Pet):
        pet.delete_instance()

    @staticmethod
    async def delete_by_id(pet_id: str) -> Pet:
        query = Pet.delete().where(Pet.pet_id == pet_id)
        query.execute()
