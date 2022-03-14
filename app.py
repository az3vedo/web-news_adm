from flask import Flask, render_template
from jinja2 import PackageLoader, Environment, select_autoescape
app = Flask(__name__)

env = Environment(
  loader=PackageLoader("app"),
  autoescape=select_autoescape()
)

@app.route('/')
def home():
  template = env.get_template('login.html')
  return render_template(template, page={'title':"Admin Login"})
