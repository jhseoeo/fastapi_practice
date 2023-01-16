from typing import List
from models.group import Group
from models.associations.users_groups import UserGroup


class GroupORM:
    @staticmethod
    async def find_by_group_id(group_id: str) -> Group:
        return Group.get_or_none(Group.group_id == group_id)

    @staticmethod
    async def save(group: Group):
        if await GroupORM.find_by_group_id(group.group_id) is not None:  # update
            group.save()
        else:  # insert
            group.save(force_insert=True)

    @staticmethod
    async def delete(group: Group):
        group.delete_instance().execute()

    @staticmethod
    async def delete_by_id(group_id: str) -> Group:
        query = Group.delete().where(Group.group_id == group_id)
        query.execute()

    @staticmethod
    async def replace_all(group_list: List[Group]) -> None:
        group_list_dict = list(map(lambda x: x.dict(), group_list))
        Group.insert_many(group_list_dict).on_conflict(
            action="update",
            conflict_target=(*Group.fields_pk(),),
            update={**Group.fields_dict_mapped_excluded()},
        ).execute()

    @staticmethod
    async def find_by_user_id(user_id: str) -> List[Group]:
        selected = Group.select().join(UserGroup).where(UserGroup.user_id == user_id)
        groups_list = [group for group in selected]
        return groups_list

    @staticmethod
    async def delete_by_id_list(group_id_list: List[str]) -> None:
        Group.delete().where(Group.group_id.in_(group_id_list)).execute()
