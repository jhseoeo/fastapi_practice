from models.user import User
from models.associations.users_groups import UserGroup
from dto.user_dto import UserDTO
from orm import postgresql
from orm.user_orm import UserORM


class UserService:
    @staticmethod
    @postgresql().atomic()
    async def addUserData(group_id: str, user_request: UserDTO):
        user = User(
            user_id=user_request.userId,
            phone_number=user_request.phoneNumber,
            any_integer=user_request.anyInteger,
            registered_date=user_request.registeredDate,
            recent_log=user_request.recentLog.dict(),
        )
        await UserORM.save(user)
        user_group = UserGroup(user_id=user_request.userId, group_id=group_id)
        user_group.save(force_insert=True)

        return user

    @staticmethod
    async def getUserData(user_id: str):
        return await UserORM.find_by_user_id(user_id=user_id)

    @staticmethod
    @postgresql().atomic()
    async def modifyUserData(user_id: str, user_request: UserDTO):
        user = await UserORM.find_by_user_id(user_id=user_id)
        user.user_id = user_request.userId
        user.phone_number = user_request.phoneNumber
        user.any_integer = user_request.anyInteger
        user.registered_date = user_request.registeredDate
        user.recent_log = user_request.recentLog.dict()
        await UserORM.save(user)

        return user

    @staticmethod
    @postgresql().atomic()
    async def deleteUserData(user_id: str):
        await UserORM.delete_by_id(user_id=user_id)
