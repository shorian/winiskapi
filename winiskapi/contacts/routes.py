from flask import Blueprint, render_template

contacts = Blueprint("contacts", __name__, url_prefix="/contacts")


@contacts.route("/new")
def new():
    return render_template("contacts/new_contact.html")
