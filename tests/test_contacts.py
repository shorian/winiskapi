import pytest
from conftest import ContactFactory


def test_GetNewContact(client):
    assert client.get("/contacts/new").status_code == 200


@pytest.mark.xfail
def test_GetContactPage(client):
    contact = ContactFactory().create()
    request = client.get(f"/contacts/{contact.slug}")
    assert request.status_code == 200
