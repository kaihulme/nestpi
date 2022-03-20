import pytest
from flask import session, g

from nestpi.db import get_db


def test_login(client, auth):
    with client:
        auth.login()
        client.get("/")
        assert session["user_id"]
        assert g.user["username"] == "test"


def test_logout(client, auth):
    with client:
        auth.login()
        auth.logout()
        assert "user_id" not in session


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (("x", "test", b"Incorrect username"), ("test", "x", b"Incorrect password")),
)
def test_invalid_login(client, auth, username, password, message):
    assert message in auth.login(username, password).data


def test_register(application, client):
    client.post("/auth/register", data={"username": "x", "password": "x"})
    with application.app_context():
        assert get_db().execute("SELECT * FROM user WHERE username = 'x'").fetchone()


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (
        ("x", "", b"Password is required"),
        ("", "x", b"Username is required"),
        ("test", "test", b"User test is already registered"),
    ),
)
def test_invalid_register(client, username, password, message):
    assert (
        message
        in client.post(
            "/auth/register", data={"username": username, "password": password}
        ).data
    )
