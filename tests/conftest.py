import os
import pytest
import tempfile

from nestpi import create_app
from nestpi.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")


@pytest.fixture
def application():
    db_fd, db_path = tempfile.mkstemp()
    application = create_app(
        {
            "TESTING": True,
            "DATABASE": db_path,
        }
    )
    with application.app_context():
        init_db()
        get_db().executescript(_data_sql)
    yield application
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(application):
    return application.test_client()


@pytest.fixture
def runner(application):
    return application.test_cli_runner()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username="test", password="test"):
        return self._client.post(
            "/auth/login", data={"username": username, "password": password}
        )

    def logout(self):
        return self._client.get("/auth/logout")


@pytest.fixture
def auth(client):
    return AuthActions(client)
