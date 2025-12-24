from flask import Blueprint, render_template, request, redirect
from flask_login import login_user
from werkzeug.security import check_password_hash
from models import User

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect("/dashboard")
        return "Invalid login"
    return render_template("login.html")
