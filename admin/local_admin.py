from flask import Blueprint, render_template, request
from models import db, User
import config

local_admin_bp = Blueprint("local_admin", __name__)

@local_admin_bp.route("/local_admin", methods=["GET","POST"])
def local_admin():
    if request.method == "POST":
        if request.form["password"] != config.LOCAL_ADMIN_PASS:
            return "Unauthorized"

        user = User.query.filter_by(uid=request.form["uid"]).first()
        if user:
            user.gas_wallet += float(request.form["amount"])
            db.session.commit()
    return render_template("local_admin.html", users=User.query.all())
