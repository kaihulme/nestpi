from nestpi import create_app


def test_config():
    """
    Check app is run in testing configuration.
    """
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    """
    Check response of home/.
    """
    response = client.get("/home/")
    assert b"Hello World!" in response.data


def test_index(client):
    """
    Check / redirects to home/.
    """
    response = client.get("/", follow_redirects=True)
    assert len(response.history) == 1
    assert response.request.path == "/home/"
