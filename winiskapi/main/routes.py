from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def hello_world():  # put application's code here
    return render_template("home.html")
