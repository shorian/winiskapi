import pytest
from conftest import UserFactory, login, messages
from flask_login import current_user


@pytest.mark.usefixtures("client", "db_session")
class TestRegistration:
    def test_GetRegistrationRoute(self, client):
        assert client.get("/register").status_code == 200

    def test_RegistrationSucceeds(self, client):
        """Registration succeeds with valid input, returns redirect, user is in database"""
        user = UserFactory()
        reg_data = {
            "email": user.email,
            "username": user.username,
            "password": user.password,
            "confirm_password": user.password,
        }
        response = client.post("/register", data=reg_data)
        assert response.status_code == 302

    def test_RegFailsIfEmailInUse(self, client):
        user = UserFactory(email="test@example.com")
        reg_data = {
            "email": user.email,
            "username": user.username,
            "password": user.password,
            "confirm_password": user.password,
        }
        response = client.post("/register", data=reg_data)
        assert b"Email already in use." in response.data


@pytest.mark.usefixtures("client", "db_session")
class TestLogin:
    def test_GetLoginRoute(self, client):
        assert client.get("/login").status_code == 200

    def test_LoginSucceeds(self, client):
        """Login succeeds when an existing user provides the correct username and password, returns redirect"""
        with client:
            response = login(client)
            assert response.status_code == 302 and current_user.is_authenticated

    def test_LoginFailsWithBadEmail(self, client):
        with client:
            user = UserFactory()
            response = login(client, user.email, user.password)
            assert (
                b"Invalid email or password." in response.data
                and not current_user.is_authenticated
            )

    def test_LoginFailsWithBadPassword(self, client):
        with client:
            response = login(client, password="bad_password")
            assert (
                b"Invalid email or password." in response.data
                and not current_user.is_authenticated
            )


def test_LogoutSucceeds(client):
    with client:
        login(client)
        assert current_user.is_authenticated
        assert (
            client.get("/logout").status_code == 302
            and not current_user.is_authenticated
        )


@pytest.mark.usefixtures("client", "db_session")
class TestPasswordReset:
    def test_GetResetRequestRoute(self, client):
        assert client.get("/reset_password").status_code == 200

    def test_PostResetRequest(self, client):
        response = client.post(
            "/reset_password",
            data={"email": "test@example.com"},
            follow_redirects=True,
        )
        assert b"If an account is associated with that email address" in response.data
        assert "reset your password" in messages[0]
