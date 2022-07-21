from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from winiskapi import db
from winiskapi.models import Contact

contacts = Blueprint("contacts", __name__, url_prefix="/contacts")


@contacts.route("/")
@login_required
def directory():
    page = request.args.get("page", 1, type=int)
    user_contacts = (
        Contact.query.filter_by(owner_id=current_user.get_id())
        .order_by(Contact.first_name, Contact.last_name)
        .paginate(page=page, per_page=20)
    )
    return render_template("contacts/directory.html", contacts=user_contacts)


@contacts.route("/new", methods=["GET", "POST"])
@login_required
def new():
    if request.method == "POST":
        contact = Contact(owner_id=current_user.get_id(), **request.json["formData"])
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template("contacts/new_contact.html")


@contacts.route("/<string:slug>")
@login_required
def view_contact(slug):
    contact = Contact.query.filter_by(slug=slug).one_or_none()
    return render_template("contacts/contact_profile.html", contact=contact)
