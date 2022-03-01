from flask import current_app
from winiskapi import create_app


def test_app_exists():
    assert current_app is not None


def test_config():
    assert not create_app("default").testing
    assert create_app("testing").testing


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Winiskapi!" in response.data
