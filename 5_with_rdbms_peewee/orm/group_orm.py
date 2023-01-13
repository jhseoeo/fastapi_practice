from models.group import Group


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
        group.delete_instance()

    @staticmethod
    async def delete_by_id(group_id: str) -> Group:
        query = Group.delete().where(Group.group_id == group_id)
        query.execute()
