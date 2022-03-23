import pytest
from winiskapi import create_app, db, mail
from winiskapi.models import User


class DummySMTP:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.is_login = False

    def starttls(self):
        return

    def login(self, user=None, password=None):
        self.is_login = True
        return

    def send_message(self, msg):
        return

    def quit(self):
        return


# Don't send real emails
messages = []


def dummy_send(msg):
    messages.clear()
    messages.append(msg.as_string())


@pytest.fixture(scope="session")
def app():
    """Create app with testing configuration, and create db tables."""
    app = create_app(cfg="testing")
    with app.app_context():

        app.config["EMAIL_CLS_SMTP"] = DummySMTP
        mail.sender.send_message = dummy_send

        db.drop_all()
        db.create_all()

        # seed with a user
        # noinspection PyArgumentList
        user = User(
            email="testuser@example.com",
            nickname="testuser",
            password="my-testing-password",
        )
        db.session.add(user)
        db.session.commit()

        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    yield app.test_client()


@pytest.fixture(scope="session")
def _db():
    """Required for pytest-flask-sqlalchemy fixtures"""
    return db


def login(
    client, email="testuser@example.com", password="my-testing-password", remember=False
):
    """Default values match test user in the database"""
    response = client.post(
        "/login",
        data={
            "email": email,
            "password": password,
            "remember": remember,
        },
    )
    return response


def register(client, email, nickname, password):
    reg_data = {
        "email": email,
        "nickname": nickname,
        "password": password,
        "confirm_password": password,
    }
    response = client.post("/register", data=reg_data)
    return response
