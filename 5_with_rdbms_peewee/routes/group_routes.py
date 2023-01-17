from fastapi import APIRouter
from services.group_service import GroupService
from dto.group_dto import GroupDTO

router = APIRouter(prefix="/group", tags=["groups"])


@router.put("/")
async def add_group_data(group: GroupDTO):
    return await GroupService.addGroupData(group_request=group)


@router.get("/{group_id}", response_model=GroupDTO)
async def get_group_data(group_id: str):
    return await GroupService.getGroupData(group_id=group_id)


@router.post("/{group_id}")
async def modify_group_data(group_id: str, group: GroupDTO):
    return await GroupService.modifyGroupData(group_id=group_id, group_request=group)


@router.get("/list/{group_id}")
async def get_group_data_by_user_id(user_id: str):
    return await GroupService.getGroupDataByUserId(user_id=user_id)


@router.post("/list/{group_id}")
async def modify_group_data(group_id: str, group: GroupDTO):
    return await GroupService.modifyGroupDataList(
        group_id=group_id, group_request=group
    )


@router.delete("/list/{group_id}")
async def delete_group_data(group_id: str):
    return await GroupService.deleteGroupDataByIdList(group_id=group_id)
