from flask import Blueprint, abort, render_template

contacts = Blueprint("contacts", __name__, url_prefix="/contacts")


@contacts.route("/new")
def new():
    return render_template("contacts/new_contact.html")


@contacts.route("/<string:slug>")
def view_contact(slug):
    abort(404)
