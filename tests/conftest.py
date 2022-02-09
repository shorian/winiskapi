import pytest
from winiskapi import create_app


@pytest.fixture
def app():
    app = create_app()
    return app
