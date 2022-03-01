from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import RegistrationForm, LoginForm

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():  # put application's code here
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(
            f"Account created for {form.nickname.data}! You can now log in.", "success"
        )
        return redirect(url_for("main.home"))
    return render_template("registration.html", title="Register", form=form)


@auth.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Welcome back!", "success")
        return redirect(url_for("main.home"))
    return render_template("login.html", form=form)
