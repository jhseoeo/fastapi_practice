from typing import Any

import peewee
from pydantic import BaseModel, Field
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class BaseDTO(BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        getter_dict = PeeweeGetterDict
