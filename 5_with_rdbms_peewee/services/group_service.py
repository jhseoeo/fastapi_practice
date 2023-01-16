from models.group import Group
from orm import postgresql
from dto.group_dto import GroupDTO
from orm.group_orm import GroupORM


class GroupService:
    @staticmethod
    @postgresql().atomic()
    async def addGroupData(group_request: GroupDTO):
        group = Group(
            group_id=group_request.groupId,
            is_report_agree=group_request.IsReportAgree,
        )
        await GroupORM.save(group)
        return group

    @staticmethod
    async def getGroupData(group_id: str):
        return await GroupORM.find_by_group_id(group_id=group_id)

    @staticmethod
    @postgresql().atomic()
    async def modifyGroupData(group_id: str, group_request: GroupDTO):
        group = await GroupORM.find_by_group_id(group_id=group_id)

        group.group_id = group_request.groupId
        group.is_report_agree = group_request.IsReportAgree
        await GroupORM.save(group)

        return group

    @staticmethod
    @postgresql().atomic()
    async def deleteGroupData(group_id: str):
        await GroupORM.delete_by_id(group_id=group_id)

    @staticmethod
    @postgresql().atomic()
    async def getGroupDataByUserId(user_id: str):
        return await GroupORM.find_by_user_id(user_id=user_id)

    @staticmethod
    @postgresql().atomic()
    async def modifyGroupDataList(group_id: str, group_request: GroupDTO):
        group_list = list(
            map(
                lambda x: Group(
                    group_id=group_request.groupId + str(x),
                    is_report_agree=False,
                ),
                [1, 2, 3],
            )
        )

        await GroupORM.replace_all(group_list=group_list)

    @staticmethod
    @postgresql().atomic()
    async def deleteGroupDataByIdList(group_id: str):
        group_id_list = [group_id + str(x) for x in [1, 2, 3]]
        await GroupORM.delete_by_id_list(group_id_list=group_id_list)
