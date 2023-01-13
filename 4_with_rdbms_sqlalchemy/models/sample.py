from .base import Base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String


class Sample(Base):
    __tablename__ = "samples"

    sample_id = Column(Integer, primary_key=True, index=True)
    sample_description = Column(String)
