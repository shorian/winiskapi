from conftest import ContactFactory, login


def test_GetNewContact(client):
    login(client)
    assert client.get("/contacts/new").status_code == 200


def test_GetContactPage(client):
    login(client)
    contact = ContactFactory().create()
    request = client.get(f"/contacts/{contact.slug}")
    assert request.status_code == 200
