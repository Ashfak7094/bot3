from flask import Flask
from flask_login import LoginManager
from models import db, User
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "login.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from auth.register import register_bp
from auth.login import login_bp
from admin.local_admin import local_admin_bp
from admin.power_admin import power_admin_bp
from routes.dashboard import dashboard_bp

app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(local_admin_bp)
app.register_blueprint(power_admin_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
