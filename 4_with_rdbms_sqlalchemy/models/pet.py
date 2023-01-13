from base import Base
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relationship


class Pet(Base):
    __tablename__ = "pets"
