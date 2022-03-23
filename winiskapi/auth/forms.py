from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError
from winiskapi.models import User


class RegistrationForm(FlaskForm):
    email = EmailField("Email", validators=[InputRequired()])
    nickname = StringField("Nickname", validators=[InputRequired(), Length(max=30)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    # noinspection PyMethodMayBeStatic
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already in use.")


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RequestResetForm(FlaskForm):
    email = EmailField("Email", validators=[InputRequired(), Email()])
    submit = SubmitField("Reset Password")


class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired(), EqualTo("password")]
    )
    submit = SubmitField("Reset Password")
