from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    nickname = StringField("Nickname", validators=[DataRequired(), Length(max=30)])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
