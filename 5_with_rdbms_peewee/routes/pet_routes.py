from fastapi import APIRouter
from services.pet_service import PetService
from dto.pet_dto import PetDTO


router = APIRouter(prefix="/pet", tags=["pets"])


@router.put("/")
async def add_pet_data(pet: PetDTO):
    return await PetService.addPetData(pet_request=pet)


@router.put("/list")
async def add_pet_list(pet: PetDTO):
    return await PetService.addPetList(pet_request=pet)


@router.get("/{pet_id}", response_model=PetDTO)
async def get_pet_data(pet_id: str):
    return await PetService.getPetData(pet_id=pet_id)


@router.get("/group/{group_id}")
async def get_pet_data_by_group_id(group_id: str):
    return await PetService.getPetDataByGroupId(group_id=group_id)


@router.post("/{pet_id}")
async def modify_pet_data(pet_id: str, pet: PetDTO):
    return await PetService.modifyPetData(pet_id=pet_id, pet_request=pet)


@router.delete("/{pet_id}")
async def delete_pet_data(pet_id: str):
    return await PetService.deletePetData(pet_id=pet_id)
