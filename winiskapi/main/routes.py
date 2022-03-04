from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.app_errorhandler(404)
def not_found(e):
    return render_template("errors/404.html"), 404


@main.app_errorhandler(500)
def internal_error(e):
    return render_template("errors/500.html"), 500


@main.app_errorhandler(403)
def forbidden(e):
    return render_template("errors/403.html"), 403
