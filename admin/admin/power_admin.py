from flask import Blueprint, render_template, request
from models import db, User
import config

power_admin_bp = Blueprint("power_admin", __name__)

@power_admin_bp.route("/power_admin", methods=["GET","POST"])
def power_admin():
    if request.method == "POST":
        if request.form["password"] != config.POWER_ADMIN_PASS:
            return "Unauthorized"

        if "reset_user" in request.form:
            user = User.query.filter_by(uid=request.form["uid"]).first()
            user.password = request.form["newpass"]
            db.session.commit()

    users = User.query.order_by(User.total_profit.desc()).all()
    return render_template("power_admin.html", users=users)
