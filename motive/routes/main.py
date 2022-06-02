from flask import Blueprint, request, render_template
from ..database.db import db
from ..models.user import User

import bcrypt

main_routes = Blueprint("example", __name__)


@main_routes.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        users = User.query.all()
        return render_template("index.html", users=users)
    else:

        email = request.form["email"]
        name = request.form["name"]
        password = request.form["password"]
        encoded_password = password.encode()
        salt = bcrypt.gensalt()
        secure_password = bcrypt.hashpw(encoded_password, salt)

        print(secure_password)

        new_listing = User(email=email, name=name, password=secure_password)
        db.session.add(new_listing)
        db.session.commit()

        users = User.query.all()
        return render_template("index.html", users=users)
