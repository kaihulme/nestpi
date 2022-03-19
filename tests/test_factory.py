from nestpi import create_app


def test_config():
    """
    Check app is run in testing configuration.
    """
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    """
    Check reponse of /hello.
    """
    response = client.get("/hello/")
    assert b"Hello World!" in response.data


def test_index(client):
    """
    Check / redirects to hello/.
    """
    response = client.get("/", follow_redirects=True)
    assert len(response.history) == 1
    assert response.request.path == "/hello/"
