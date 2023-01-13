from fastapi import APIRouter
from services.user_service import UserService
from dto.user_dto import UserDTO


router = APIRouter(prefix="/user", tags=["users"])


@router.put("/")
async def add_user_data(group_id: str, user: UserDTO):
    return await UserService.addUserData(group_id=group_id, user_request=user)


@router.get("/{user_id}", response_model=UserDTO)
async def get_user_data(user_id: str):
    return await UserService.getUserData(user_id=user_id)


@router.post("/{user_id}")
async def modify_user_data(user_id: str, user: UserDTO):
    return await UserService.modifyUserData(user_id=user_id, user_request=user)


@router.delete("/{user_id}")
async def delete_user_data(user_id: str):
    return await UserService.deleteUserData(user_id=user_id)
