def test_registration(client):
    assert client.get("/register").status_code == 200
