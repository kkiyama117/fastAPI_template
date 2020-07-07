import pytest
from fastapi.testclient import TestClient

from portfolio_api.db import connection, engine
from portfolio_api.db.user.schema import UserSchema
from portfolio_api.core import initializer
from portfolio_api import app


def create_test_client():
    _app = app.create_app()
    initializer.initialize()
    # Override database
    cli = TestClient(_app)
    return cli


# Drop database data
def drop_db():
    # Delete users
    users = UserSchema().get_table()
    query = users.drop(engine)
    connection.execute(query)


@pytest.fixture(scope="module", autouse=True)
def scope_module():
    # run create test client and yield data
    cli = create_test_client()
    yield cli
    # teardown

    drop_db()
    print("test teardown end")
