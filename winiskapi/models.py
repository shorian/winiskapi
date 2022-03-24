from winiskapi import db, login_manager, argon2
from flask import current_app
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
import uuid
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(160), unique=True, nullable=False, index=True)
    nickname = db.Column(db.String(30))
    pw_hash = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.Date, default=datetime.today)
    contacts = db.relationship(
        "Contact",
        primaryjoin="User.id==Contact.owner_id",
        backref="users",
        cascade="all,delete,delete-orphan",
    )
    self_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("contacts.id", use_alter=True, name="fk_self_contact_id"),
    )
    self_contact = db.relationship("Contact", primaryjoin="User.self_id==Contact.id")

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.pw_hash = argon2.generate_password_hash(password)

    def verify_password(self, password):
        return argon2.check_password_hash(self.pw_hash, password)

    def generate_reset_token(self):
        s = Serializer(current_app.config["SECRET_KEY"], salt=b"reset")
        return s.dumps({"reset": self.id.hex})

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config["SECRET_KEY"], salt=b"reset")
        try:
            data = s.loads(token, max_age=3600)
        except:
            return False
        user = User.query.get(data.get("reset"))
        if user is None:
            return False
        user.password = new_password
        db.session.commit()
        return True

    def __repr__(self):
        return f"User('{self.nickname}', '{self.email}'')"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Contact(db.Model):
    __tablename__ = "contacts"
    owner_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("users.id", use_alter=True, name="fk_contact_owner_id"),
    )
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date_created = db.Column(db.Date, default=datetime.today)

    surname = db.Column(db.String(30))
    given_name = db.Column(db.String(30))
    middle_name = db.Column(db.String(30))
    nickname = db.Column(db.String(30))
    picture = db.Column(db.String(16), nullable=False, default="default.png")
    dob = db.Column(db.Date())
    # pronouns = db.Column(db.???()) Not sure what datatype pronouns should be. String? Enum? Array?)
    organization = db.Column(db.String(50))
    occupation = db.Column(db.String(50))
    food_preferences = db.Column(db.Text())
