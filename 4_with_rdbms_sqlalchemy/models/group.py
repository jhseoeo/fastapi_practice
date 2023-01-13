from base import Base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Boolean
from sqlalchemy.orm import relationship

from associations.users_groups import users_groups


class Group(Base):
    __tablename__ = "groups"

    id = Column(String(36), primary_key=True)
    is_report_agree = Column(Boolean())

    users = relationship("Users", secondary=users_groups, back_populates="groups")
