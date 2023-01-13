from playhouse.postgres_ext import BooleanField, ForeignKeyField
from models import BaseModel, group


class Subscription(BaseModel):
    group_id = ForeignKeyField(
        group.Group,
        backref="subscriptions",
        primary_key=True,
    )
    some_data = BooleanField()

    class Meta:
        db_table = "subscriptions"
