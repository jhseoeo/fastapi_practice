from fastapi import APIRouter
from services.subscription_service import SubscriptionService
from dto.subscription_dto import SubscriptionDTO


router = APIRouter(prefix="/subscription", tags=["subscriptions"])


@router.put("/")
async def add_subscription_data(subscription: SubscriptionDTO):
    return await SubscriptionService.addSubscriptionData(
        subscription_request=subscription
    )


@router.get("/{group_id}", response_model=SubscriptionDTO)
async def get_subscription_data(group_id: str):
    return await SubscriptionService.getSubscriptionData(group_id=group_id)


@router.post("/{group_id}")
async def modify_subscription_data(group_id: str, subscription: SubscriptionDTO):
    return await SubscriptionService.modifySubscriptionData(
        group_id=group_id, subscription_request=subscription
    )


@router.delete("/{group_id}")
async def delete_subscription_data(group_id: str):
    return await SubscriptionService.deleteSubscriptionData(group_id=group_id)
