import pytest
from winiskapi import create_app, db
from winiskapi.models import User


@pytest.fixture(scope="session")
def app():
    """Create app with testing configuration, and create db tables."""
    app = create_app(cfg="testing")
    with app.app_context():
        db.create_all()

        # seed with a user
        # noinspection PyArgumentList
        user = User(
            email="testuser@example.com",
            nickname="testuser",
            password="my-testing-password",
        )
        db.session.add(user)
        db.session.commit()

        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    yield app.test_client()


@pytest.fixture(scope="session")
def _db():
    """Required for pytest-flask-sqlalchemy fixtures"""
    return db
