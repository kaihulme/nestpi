import pytest
import sqlite3

from nestpi.db import get_db


def test_db_connection(app):
    """
    Check app connects to database.
    """
    with app.app_context():
        db = get_db()
        db.execute("SELECT 1")


def test_is_same_db(app):
    """
    Check app always connects to same database.
    """
    with app.app_context():
        db = get_db()
        assert db is get_db()


def test_db_is_closed(app):
    """
    Check database is closed outside app context.
    """
    with app.app_context():
        db = get_db()
    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute("SELECT 1")
    assert "closed" in str(e.value)


def test_db_has_user_table(app):
    """
    Check database has users table.
    """
    with app.app_context():
        db = get_db()
        db.execute("SELECT * FROM user")
