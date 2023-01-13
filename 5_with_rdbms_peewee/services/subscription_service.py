from models.subscription import Subscription
from dto.subscription_dto import SubscriptionDTO
from orm import postgresql
from orm.subscription_orm import SubscriptionORM


class SubscriptionService:
    @staticmethod
    @postgresql().atomic()
    async def addSubscriptionData(subscription_request: SubscriptionDTO):
        subscription = Subscription(
            group_id=subscription_request.groupId,
            some_data=subscription_request.someData,
        )
        await SubscriptionORM.save(subscription)
        return subscription

    @staticmethod
    async def getSubscriptionData(group_id: str):
        return await SubscriptionORM.find_by_group_id(group_id=group_id)

    @staticmethod
    @postgresql().atomic()
    async def modifySubscriptionData(
        group_id: str, subscription_request: SubscriptionDTO
    ):
        subscription = await SubscriptionORM.find_by_group_id(group_id=group_id)

        subscription.group_id = subscription_request.groupId
        subscription.some_data = subscription_request.someData
        await SubscriptionORM.save(subscription)

        return subscription

    @staticmethod
    @postgresql().atomic()
    async def deleteSubscriptionData(group_id: str):
        await SubscriptionORM.delete_by_id(group_id=group_id)
