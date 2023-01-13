from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

## temporary
from dotenv import load_dotenv
import os

from models import sample


load_dotenv()


class DBUninitializedException(BaseException):
    pass


class PostgreSQL:
    def __init__(self):
        HOST = os.environ.get("DB_HOST")
        PORT = os.environ.get("DB_PORT")
        ID = os.environ.get("DB_ID")
        PW = os.environ.get("DB_PW")
        DB = os.environ.get("DB_DB")

        self.__url = "postgresql://{}:{}@{}:{}/{}".format(ID, PW, HOST, PORT, DB)
        self.__session = None

    def __call__(self):
        if self.__session is not None:
            return self.__session
        else:
            raise DBUninitializedException()

    def connect(self):
        engine = create_engine(self.__url)

        sample.Sample.__table__.create(bind=engine, checkfirst=True)

        Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.__session = Session()

    def close(self):
        self.__session.close()


postgresql = PostgreSQL()
