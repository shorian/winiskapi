from flask import current_app

from winiskapi import create_app


def test_AppExists():
    assert current_app is not None


def test_ConfigIsTesting(client):
    with client:
        assert current_app.config["TESTING"] == True


def test_DefaultConfigIsDev():
    app = create_app()
    assert app.config["DEBUG"] == True and app.config["SECRET_KEY"] == "my dev key"


def test_HomeRouteExists(client):
    response = client.get("/")
    assert response.status_code == 200 and b"Welcome to Winiskapi!" in response.data
