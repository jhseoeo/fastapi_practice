from models.subscription import Subscription


class SubscriptionORM:
    @staticmethod
    async def find_by_group_id(group_id: str) -> Subscription:
        return Subscription.get_or_none(Subscription.group_id == group_id)

    @staticmethod
    async def save(subscription: Subscription):
        if await SubscriptionORM.find_by_group_id(subscription.group_id) is not None:
            subscription.save()
        else:
            subscription.save(force_insert=True)

    @staticmethod
    async def delete(subscription: Subscription):
        subscription.delete_instance()

    @staticmethod
    async def delete_by_id(group_id: str) -> Subscription:
        query = Subscription.delete().where(Subscription.group_id == group_id)
        query.execute()
