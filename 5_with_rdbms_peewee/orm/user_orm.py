from models.user import User


class UserORM:
    @staticmethod
    async def find_by_user_id(user_id: str) -> User:
        return User.get_or_none(User.user_id == user_id)

    @staticmethod
    async def save(user: User):
        if await UserORM.find_by_user_id(user.user_id) is not None:
            user.save()
        else:
            user.save(force_insert=True)

    @staticmethod
    async def delete(user: User):
        user.delete_instance()

    @staticmethod
    async def delete_by_id(user_id: str) -> User:
        query = User.delete().where(User.user_id == user_id)
        query.execute()
