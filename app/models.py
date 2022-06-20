from flask_login import UserMixin
from app import db


class Login(UserMixin, db.Model):
  __tablename__ = "login"
  id = db.Column(db.Integer, primary_key=True)
  userName = db.Column(db.String(80), unique=True, nullable=False)
  senha = db.Column(db.String(80), nullable=False)