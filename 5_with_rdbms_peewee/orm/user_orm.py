from models.user import User


class UserORM:
    @staticmethod
    async def find_by_user_id(user_id: str) -> User:
        return User.get_or_none(User.user_id == user_id)

    @staticmethod
    async def save(user: User):
        User.insert(user.dict()).on_conflict(
            action="update",
            conflict_target=(*User.fields_pk(),),
            update={**user.field_dict()},
        ).execute()

    @staticmethod
    async def delete(user: User):
        user.delete_instance()

    @staticmethod
    async def delete_by_id(user_id: str) -> User:
        query = User.delete().where(User.user_id == user_id)
        query.execute()
