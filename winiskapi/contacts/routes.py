from flask import Blueprint, abort, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from winiskapi import db
from winiskapi.models import Contact

contacts = Blueprint("contacts", __name__, url_prefix="/contacts")


@contacts.route("/new", methods=["GET", "POST"])
@login_required
def new():
    if request.method == "POST":
        # form_data = request.json["formData"]
        # if form_data["contact_info"]:
        #   contact_info = form_data.pop("contact_info")
        #   for i in contact_info:
        #       add that info to the db, with appropriate destructuring
        # and so on for other contact fields, until only attributes belonging to the contact table proper are left
        contact = Contact(owner_id=current_user.get_id(), **request.json["formData"])
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template("contacts/new_contact.html")


@contacts.route("/<string:slug>")
@login_required
def view_contact(slug):
    abort(404)
