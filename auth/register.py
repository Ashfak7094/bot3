from flask import Blueprint, render_template, request, redirect
from werkzeug.security import generate_password_hash
from models import db, User
import uuid, config

register_bp = Blueprint("register", __name__)

@register_bp.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        if request.form["password"] != request.form["repass"]:
            return "Passwords not matching"

        user = User(
            uid=str(uuid.uuid4())[:8],
            title=request.form["title"],
            nickname=request.form["nickname"],
            username=request.form["username"],
            mobile=request.form["mobile"],
            password=generate_password_hash(request.form["password"]),
            gas_wallet=config.TRIAL_GAS,
            referred_by=request.form.get("refcode",""),
            referral_code=str(uuid.uuid4())[:6]
        )
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html")
