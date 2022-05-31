from flask import Blueprint, abort, render_template
from flask_login import login_required

contacts = Blueprint("contacts", __name__, url_prefix="/contacts")


@contacts.route("/new", methods=["GET", "POST"])
@login_required
def new():
    return render_template("contacts/new_contact.html")


@contacts.route("/<string:slug>")
@login_required
def view_contact(slug):
    abort(404)
