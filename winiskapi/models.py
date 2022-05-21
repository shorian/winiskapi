import sqlalchemy as sa
from flask import current_app
from flask_login import UserMixin
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from slugify import slugify
from sqlalchemy.dialects.postgresql import JSONB, UUID
from ulid import ULID

from winiskapi import argon2, db, login_manager


def ulid_as_uuid():
    """Generate a ULID and store as UUID for use as a sortable primary key"""
    ulid = ULID()
    return ulid.to_uuid()


def build_slug(context):
    """Build a url slug using the contact's name and primary key.
    Rebuild whenever the contact's name changes."""
    pk = context.get_current_parameters()["id"]
    pk = str(pk)[30:36]
    names = [
        context.get_current_parameters().get(key)
        for key in ["first_name", "middle_name", "last_name", "nickname"]
    ]
    names = " ".join(filter(None, names))
    slug = slugify(
        names, max_length=30, word_boundary=True, lowercase=False, allow_unicode=True
    )
    return f"{pk}-{slug}"


class TimestampsMixin:
    """Mixin that defines timestamp columns."""

    __abstract__ = True

    created_at = sa.Column(
        "created_at",
        sa.TIMESTAMP(timezone=True),
        default=sa.func.now(),
        nullable=False,
    )

    updated_at = sa.Column(
        "last_updated",
        sa.TIMESTAMP(timezone=True),
        default=sa.func.now(),
        onupdate=sa.func.now(),
        nullable=False,
    )


class User(UserMixin, db.Model, TimestampsMixin):
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=ulid_as_uuid)
    email = db.Column(db.String(160), unique=True, nullable=False, index=True)
    username = db.Column(db.String(30), nullable=False)
    pw_hash = db.Column(db.String(), nullable=False)
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
        return f"User('{self.username}', '{self.email}'')"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Contact(db.Model, TimestampsMixin):
    __tablename__ = "contacts"
    owner_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("users.id", use_alter=True, name="fk_contact_owner_id"),
    )
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=ulid_as_uuid)
    slug = db.Column(db.String(40), default=build_slug, unique=True, nullable=False)

    first_name = db.Column(db.String(30), nullable=False)
    middle_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    nickname = db.Column(db.String(30))
    picture = db.Column(db.String(16), nullable=False, default="default.png")
    dob = db.Column(db.Date())
    gender = db.Column(db.Enum("U", "N", "M", "F", name="gender"), server_default="U")
    pronouns = db.Column(db.ARRAY(db.String(15)))
    organization = db.Column(db.String(50))
    job_title = db.Column(db.String(50))
    notes = db.Column(db.Text())

    contact_fields = db.relationship(
        "ContactFields",
        primaryjoin="Contact.id==ContactFields.contact_id",
        cascade="all,delete,delete-orphan",
    )


class ContactFields(db.Model):
    __tablename__ = "contact_fields"
    owner_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("users.id", use_alter=True, name="fk_field_owner_id"),
    )
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("contacts.id"), nullable=False
    )
    section = db.Column(db.String(30), nullable=False)
    value = db.Column(JSONB(), nullable=False)
