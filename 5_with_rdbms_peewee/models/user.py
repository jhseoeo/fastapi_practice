from playhouse.postgres_ext import (
    IntegerField,
    CharField,
    TextField,
    TimestampField,
    BinaryJSONField,
)
from models import BaseModel


class User(BaseModel):
    user_id = CharField(max_length=36, primary_key=True)
    phone_number = TextField(unique=True, null=False, index=True)
    any_integer = IntegerField()
    registered_date = TimestampField()
    recent_log = BinaryJSONField(index=False)

    class Meta:
        db_table = "users"
