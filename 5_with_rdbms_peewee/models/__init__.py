from __future__ import annotations
from typing import List, Dict, Any

from playhouse.postgres_ext import Model, Field, EXCLUDED
from orm import postgresql


class BaseModel(Model):
    @classmethod
    def fields(cls) -> List[Field]:
        return list(cls._meta.fields.values())

    @classmethod
    def fields_pk(cls) -> List[Field]:
        fields = cls.fields()
        wo_pk = filter(lambda x: x.primary_key, fields)
        return list(wo_pk)

    @classmethod
    def fields_dict_mapped_excluded(cls) -> List[Field]:
        result = dict()
        for fieldname in cls._meta.fields:
            if not cls._meta.fields[fieldname].primary_key:
                result.update(
                    {cls._meta.fields[fieldname]: EXCLUDED.__getattr__(fieldname)}
                )
        return result

    def dict(self) -> Dict[str, Any]:
        return self.__data__

    def field_dict(self) -> Dict[Field, Any]:
        result = dict()
        columns = self.dict()
        for fieldname in self._meta.fields:
            if not self._meta.fields[fieldname].primary_key:
                result.update({self._meta.fields[fieldname]: columns[fieldname]})
        return result

    class Meta:
        database = postgresql()
