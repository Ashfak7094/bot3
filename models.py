from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(12), unique=True)
    title = db.Column(db.String(10))
    nickname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    mobile = db.Column(db.String(20))
    password = db.Column(db.String(200))

    api_key = db.Column(db.String(200))
    api_secret = db.Column(db.String(200))

    gas_wallet = db.Column(db.Float, default=1.00)
    total_profit = db.Column(db.Float, default=0.0)

    referral_code = db.Column(db.String(20))
    referred_by = db.Column(db.String(20))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_uid = db.Column(db.String(12))
    level = db.Column(db.Integer)
    reward = db.Column(db.Float)
