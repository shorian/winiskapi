import pytest
from faker import Faker

from winiskapi import create_app, db, mail
from winiskapi.models import Contact, User

fake = Faker()
Faker.seed(0)


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
        user = User(
            email="test@example.com",
            username="testuser",
            password="test-password",
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


class UserFactory:
    def __init__(self, **kwargs):
        """Generate random user attributes.
        Use keyword arguments to override generated values.
        """
        self.email = fake.unique.email()
        self.username = fake.user_name()
        self.password = fake.password()

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def create(self):
        """Commit to the db, and return the user object."""
        user = User(**self.__dict__)
        db.session.add(user)
        db.session.commit()
        return user


class ContactFactory:
    def __init__(self, complete=False, **kwargs):
        """Generate random contact attributes.
        Set an attribute manually with a keyword argument.
        At least one user must exist in the db before creating a contact.
        """
        self.owner_id = User.query.filter_by(email="test@example.com").first().id
        self.first_name = fake.first_name()

        if complete:
            self.last_name = fake.last_name()
            self.middle_name = fake.first_name()
            self.nickname = fake.first_name()
            self.dob = fake.date_of_birth()
            self.gender = fake.random_element(
                elements=("", "Male", "Female", "Nonbinary")
            )
            self.pronouns = fake.random_element(
                elements=(
                    ["he", "him", "his", "his", "himself"],
                    ["she", "her", "her", "hers", "herself"],
                    ["they", "them", "their", "theirs", "themself"],
                ),
            )
            self.organization = fake.company()
            self.job_title = fake.job()
            self.bio = fake.paragraph()

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def create(self):
        """Commit to the db, and return the contact object."""
        contact = Contact(**self.__dict__)
        db.session.add(contact)
        db.session.commit()
        return contact


def login(client, email="test@example.com", password="test-password", remember=False):
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


class DummySMTP:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.is_login = False

    def starttls(self):
        return

    # noinspection PyUnusedLocal
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
    messages.append(msg.as_string())
