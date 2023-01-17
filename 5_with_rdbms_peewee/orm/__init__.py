import peewee
from playhouse.postgres_ext import PostgresqlExtDatabase
from contextvars import ContextVar
import functools

## temporary
from dotenv import load_dotenv
import os

load_dotenv()


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        db_state_default = {
            "closed": None,
            "conn": None,
            "ctx": None,
            "transactions": None,
        }
        db_state = ContextVar("db_state", default=db_state_default)
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


class PostgreSQL:
    def __init__(self):
        HOST = os.environ.get("DB_HOST")
        PORT = os.environ.get("DB_PORT")
        ID = os.environ.get("DB_ID")
        PW = os.environ.get("DB_PW")
        DB = os.environ.get("DB_DB")
        self.__db = PostgresqlExtDatabase(
            DB, host=HOST, port=PORT, user=ID, password=PW
        )
        self.__db._state = PeeweeConnectionState()

    def __call__(self):
        return self.__db


postgresql = PostgreSQL()
