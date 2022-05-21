import pytest
from conftest import ContactFactory, UserFactory


@pytest.mark.usefixtures("client", "db_session")
class TestUserModel:
    def test_CreateUser(self):
        user = UserFactory().create()
        assert user.id


@pytest.mark.usefixtures("client", "db_session")
class TestContactModel:
    def test_CreateContact(self):
        contact = ContactFactory().create()
        assert contact.id and contact.owner_id
