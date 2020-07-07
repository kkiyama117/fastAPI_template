import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from portfolio_api.core import config


# Use for test
def get_db_connection():
    return databases.Database(config.SQLALCHEMY_DATABASE_URI)


def get_db_engine():
    uri = config.SQLALCHEMY_DATABASE_URI
    return sqlalchemy.create_engine(uri, connect_args={"check_same_thread": False})


# used as database connection
connection = get_db_connection()
# schema meta data
metadata = sqlalchemy.MetaData()
SchemaBase = declarative_base(metadata=metadata)
# used to create first schema
engine = get_db_engine()
