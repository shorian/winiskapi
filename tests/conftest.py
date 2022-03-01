import pytest
from winiskapi import create_app


@pytest.fixture
def app():
    app = create_app("testing")
    # import and create db
    return app


@pytest.fixture
def client(app):
    return app.test_client()
