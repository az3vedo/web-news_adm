from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_user, logout_user, login_required
from app.services.login import LoginService

login_service = LoginService()

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
  login_response = login_service.doLogin(request.get_json())
  if not login_response:
    return redirect(url_for('main.index'))
  return redirect(url_for('main.news_control'))

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))