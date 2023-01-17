from typing import List
from models.pet import Pet


class PetORM:
    @staticmethod
    async def find_by_pet_id(pet_id: str) -> Pet:
        return Pet.get_or_none(Pet.pet_id == pet_id)

    @staticmethod
    async def save(pet: Pet):
        Pet.insert(pet.dict()).on_conflict(
            action="update",
            conflict_target=(*Pet.fields_pk(),),
            update={**pet.field_dict()},
        ).execute()

    @staticmethod
    async def save_all(pet_list: List[Pet]):
        pet_list_dict = list(map(lambda x: x.dict(), pet_list))
        Pet.insert_many(pet_list_dict).execute()

    @staticmethod
    async def delete(pet: Pet):
        pet.delete_instance()

    @staticmethod
    async def delete_by_id(pet_id: str) -> Pet:
        query = Pet.delete().where(Pet.pet_id == pet_id)
        query.execute()

    @staticmethod
    async def find_by_group_id(group_id: str) -> List[Pet]:
        selected = Pet.select().where(Pet.group_id == group_id)
        pets = [pet for pet in selected]
        return pets
