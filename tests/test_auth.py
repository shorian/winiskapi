import pytest
from winiskapi.models import User
from flask_login import current_user


def register(client, email, nickname, password):
    reg_data = {
        "email": email,
        "nickname": nickname,
        "password": password,
        "confirm_password": password,
    }
    response = client.post("/register", data=reg_data)
    return response


@pytest.mark.usefixtures("client", "db_session")
class TestRegistration:
    def test_RegistrationRouteExists(self, client):
        assert client.get("/register").status_code == 200

    def test_RegistrationSucceeds(self, client):
        """Registration succeeds with valid input, returns redirect, user is in database"""
        email = "john@example.com"
        password = "123456"
        response = register(client, email, "john", password)
        user = User.query.filter_by(email=email).first()
        assert response.status_code == 302
        assert user.pw_hash != password
        assert user.date_created is not None

    def test_RegFailsForExistingUser(self, client):
        response = register(client, "testuser@example.com", "alice", "alicespassword")
        assert b"Email already in use." in response.data


def login(client, email, password, remember=False):
    response = client.post(
        "/login",
        data={
            "email": email,
            "password": password,
            "remember": remember,
        },
    )
    return response


@pytest.mark.usefixtures("client", "db_session")
class TestLogin:
    def test_LoginRouteExists(self, client):
        assert client.get("/login").status_code == 200

    def test_LoginSucceeds(self, client):
        """Login succeeds when an existing user provides the correct username and password, returns redirect"""
        with client:
            response = login(client, "testuser@example.com", "my-testing-password")
            assert response.status_code == 302 and current_user.is_authenticated

    def test_LoginFailsWithBadEmail(self, client):
        with client:
            response = login(client, "notauser@example.com", "bad_password")
            assert (
                b"Invalid email or password." in response.data
                and not current_user.is_authenticated
            )

    def test_LoginFailsWithBadPassword(self, client):
        with client:
            response = login(client, "testuser@example.com", "bad_password")
            assert (
                b"Invalid email or password." in response.data
                and not current_user.is_authenticated
            )


def test_LogoutSucceeds(client):
    with client:
        login(client, "testuser@example.com", "my-testing-password")
        assert current_user.is_authenticated
        assert (
            client.get("/logout").status_code == 302
            and not current_user.is_authenticated
        )
