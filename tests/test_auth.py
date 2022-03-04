def test_registration(client, app):
    assert client.get("/register").status_code == 200
    reg_data = {
        "email": "john@example.com",
        "nickname": "john",
        "password": "123456",
        "confirm_password": "123456",
    }
    response = client.post("/register", data=reg_data)
    assert response.status_code == 302  # redirects don't work for some reason


def test_login(client):
    assert client.get("/login").status_code == 200
    response = client.post(
        "/login",
        data={"email": "john@example.com", "password": "123456", "remember": "false"},
    )
    assert response.status_code == 302


def test_logout(client):
    assert client.get("/logout").status_code == 302
