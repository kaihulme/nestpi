from nestpi.db import get_db


def test_is_same_db(app):
    """
    Check app always connects to same database.
    """
    with app.app_context():
        db = get_db()
        assert db is get_db()
