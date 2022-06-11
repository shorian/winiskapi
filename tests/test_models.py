from datetime import datetime, timedelta, timezone

import pytest
from conftest import ContactFactory, UserFactory
from freezegun import freeze_time


@pytest.mark.usefixtures("client")
class TestUserModel:
    def test_CreateUser(self):
        user = UserFactory().create()
        assert user.id

    def test_HasPasswordHash(self):
        user = UserFactory().create()
        assert user.pw_hash

    def test_PasswordIsNotReadable(self):
        user = UserFactory().create()
        with pytest.raises(AttributeError):
            # noinspection PyStatementEffect
            user.password

    def test_PasswordIsHashed(self):
        user = UserFactory(password="my_password").create()
        assert user.pw_hash != "my_password"

    def test_CanVerifyPassword(self):
        user = UserFactory(password="my_password").create()
        assert user.verify_password("my_password")
        assert not user.verify_password("not_my_password")

    def test_SaltsAreRandom(self):
        user1 = UserFactory(password="password").create()
        user2 = UserFactory(password="password").create()
        assert user1.pw_hash != user2.pw_hash

    def test_CanResetPassword(self):
        user = UserFactory(password="forgotten_password").create()
        token = user.generate_reset_token()
        assert user.reset_password(token, "my_new_password")
        assert user.verify_password("my_new_password")

    def test_ExpiredResetTokenFails(self, client):
        with freeze_time(datetime.now()) as current_time:
            user = UserFactory(password="forgotten_password").create()
            token = user.generate_reset_token()
            current_time.tick(delta=timedelta(minutes=61))
            assert not user.reset_password(token, "my_new_password")

    def test_UserTimestamps(self):
        user = UserFactory().create()
        now = datetime.now(timezone.utc)
        assert (now - user.created_at).total_seconds() < 2
        assert (now - user.last_updated).total_seconds() < 2


@pytest.mark.usefixtures("client")
class TestContactModel:
    def test_CreateContact(self):
        contact = ContactFactory().create()
        assert contact.id and contact.owner_id

    def test_CreateCompleteContact(self):
        contact = ContactFactory(complete=True).create()
        assert contact.id and contact.slug

    def test_ContactTimestamps(self):
        contact = ContactFactory().create()
        now = datetime.now(timezone.utc)
        assert (now - contact.created_at).total_seconds() < 2
        assert (now - contact.last_updated).total_seconds() < 2
