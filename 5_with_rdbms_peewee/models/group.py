from playhouse.postgres_ext import CharField, BooleanField
from models import BaseModel


class Group(BaseModel):
    group_id = CharField(max_length=36, primary_key=True, index=True)
    is_report_agree = BooleanField()

    class Meta:
        db_table = "groups"
