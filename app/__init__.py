from flask import Flask, render_template, request, redirect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from jinja2 import PackageLoader, Environment, select_autoescape

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:12345@localhost:3307/web-news-adm"
  app.config['SECRET_KEY'] = 'secret'
  db.init_app(app)

  from app.routes.auth import auth
  from app.routes.main import main
  from app.models import Login

  with app.app_context():
    db.create_all()

  app.register_blueprint(auth)
  app.register_blueprint(main)

  login_manager = LoginManager()
  login_manager.login_view = 'main.index'
  login_manager.init_app(app)

  @login_manager.user_loader
  def user_loader(user_id):
    return Login.query.get(int(user_id))
  
  return app