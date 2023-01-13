from peewee import IntegerField, CharField
from models import BaseModel


class Sample(BaseModel):
    sample_id = IntegerField(primary_key=True, index=True)
    sample_description = CharField(null=True, unique=True, default="ㄴㄴ")

    class Meta:
        db_table = "samples"
