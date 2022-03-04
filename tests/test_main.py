from flask import current_app
from winiskapi import create_app


def test_app_exists():
    assert current_app is not None


def test_config():
    app = create_app()
    assert app.config["DEBUG"] == True
    assert app.config["SECRET_KEY"] == "my dev key"


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Winiskapi!" in response.data
