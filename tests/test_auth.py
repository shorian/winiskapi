def test_registration(client):
    assert client.get("/register").status_code == 200
    response = client.post(
        "/register",
        data={
            "email": "john@example.com",
            "nickname": "john",
            "password": "cat",
            "confirm_password": "cat",
        },
    )
    assert response.status_code == 200


def test_login(client):
    assert client.get("/login").status_code == 200
    response = client.post(
        "/login",
        data={"email": "john@example.com", "password": "cat", "remember": "false"},
    )
    assert response.status_code == 200
