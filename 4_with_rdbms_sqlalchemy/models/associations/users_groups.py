from ..base import Base
from sqlalchemy import Column, ForeignKey, Table


users_groups = Table(
    "users_groups",
    Base.metadata,
    Column("user_id", ForeignKey("users.user_id")),
    Column("group_id", ForeignKey("groups.group_id")),
)
