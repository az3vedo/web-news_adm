from flask import Flask, render_template, request, redirect
from jinja2 import PackageLoader, Environment, select_autoescape
from routes.auth import auth
from routes.main import main
app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(main)
