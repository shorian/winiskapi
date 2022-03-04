from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required
from winiskapi import db
from winiskapi.models import User
from .forms import RegistrationForm, LoginForm


auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():  # put application's code here
    form = RegistrationForm()
    if form.validate_on_submit():
        # noinspection PyArgumentList
        user = User(
            email=form.email.data,
            nickname=form.nickname.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        flash(
            f"Account created for {form.nickname.data}! You can now log in.", "success"
        )
        return redirect(url_for(".login"))
    return render_template("registration.html", title="Register", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            flash("Welcome back!", "success")
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            flash("Invalid email or password.")
    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("main.home"))
