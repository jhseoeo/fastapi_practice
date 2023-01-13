from playhouse.postgres_ext import Model
from orm import postgresql


class BaseModel(Model):
    class Meta:
        database = postgresql()
