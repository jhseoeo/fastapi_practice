from base import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime, JSON, ARRAY
from sqlalchemy.orm import relationship

from associations.users_groups import users_groups


class User(Base):
    __tablename__ = "users"

    user_id = Column(String(36), primary_key=True, index=True)
    phone_number = Column(String, index=True, unique=True, nullable=False)
    any_integer = Column(Integer)
    registered_date = Column(DateTime)
    recent_log = Column(JSON)
    terms = Column(ARRAY(JSON))

    groups = relationship("Groups", secondary=users_groups, back_populates="users")
