import pytest
from winiskapi import create_app


@pytest.fixture
def app():
    app = create_app(cfg="testing")

    yield app


@pytest.fixture
def client(app):
    yield app.test_client()
