from base import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relationship


class Subscription(Base):
    __tablename__ = "subscriptions"

    group_id = Column(
        String(36),
        ForeignKey("groups.group_id"),
        primary_key=True,
    )
    some_data = Column(String)
