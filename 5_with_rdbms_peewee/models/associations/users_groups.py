from playhouse.postgres_ext import ForeignKeyField, CompositeKey
from models import BaseModel, group, user


class UserGroup(BaseModel):
    group_id = ForeignKeyField(group.Group, backref="user_group", index=True)
    user_id = ForeignKeyField(user.User, backref="user_group", index=True)

    class Meta:
        db_table = "user_groups"
        primary_key = CompositeKey("user_id", "group_id")
