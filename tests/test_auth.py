import pytest
from freezegun import freeze_time
from datetime import datetime, timedelta
from winiskapi.models import User
from flask_login import current_user
from conftest import login, register, messages


@pytest.mark.usefixtures("client", "db_session")
class TestRegistration:
    def test_GetRegistrationRoute(self, client):
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
            response = login(
                client, email="notauser@example.com", password="my_password"
            )
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
            data={"email": "testuser@example.com"},
            follow_redirects=True,
        )
        assert b"If an account is associated with that email address" in response.data
        assert "reset your password" in messages[0]

    def test_GoodResetTokenSucceeds(self, client):
        user = User.query.filter_by(email="testuser@example.com").first()
        token = user.generate_reset_token()
        assert user.reset_password(token, "my-new-password")

        with client:
            login(client, password="my-new-password")
            assert current_user.is_authenticated

    def test_ExpiredResetTokenFails(self, client):
        with freeze_time(datetime.now()) as current_time:
            user = User.query.filter_by(email="testuser@example.com").first()
            token = user.generate_reset_token()
            current_time.tick(delta=timedelta(minutes=61))
            assert not user.reset_password(token, "my-new-password")

        with client:
            login(client, password="my-new-password")
            assert not current_user.is_authenticated
