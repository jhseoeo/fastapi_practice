from playhouse.postgres_ext import CharField, IntegerField, ForeignKeyField
from models import BaseModel, group


class Pet(BaseModel):
    pet_id = CharField(max_length=36, primary_key=True, index=True)
    group_id = ForeignKeyField(group.Group, backref="pets")
    some_fields = IntegerField()

    class Meta:
        db_table = "pets"
