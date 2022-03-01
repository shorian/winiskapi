from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def home():  # put application's code here
    return render_template("home.html")
