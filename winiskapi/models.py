from winiskapi import db, login_manager, argon2
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(UserMixin, db.Model):  # add UserMixin later
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(120), unique=True, index=True)
    nickname = db.Column(db.String(30))
    pw_hash = db.Column(db.String())
    date_created = db.Column(db.TIMESTAMP, default=func.now())

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.pw_hash = argon2.generate_password_hash(password)

    def verify_password(self, password):
        return argon2.check_password_hash(self.pw_hash, password)

    def __repr__(self):
        return f"User('{self.nickname}', '{self.email}'')"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
