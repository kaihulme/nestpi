from flask import session, g


def test_login(client, auth):
    auth.login()
    with client:
        client.get("/")
        assert session["user_id"]
        assert g.user["username"] == "test"
