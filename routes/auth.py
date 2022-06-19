from flask import Blueprint, render_template
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():

  return render_template('login.html', page={'title': "Login"})

@auth.route('/logout')
def logout():
  return 'Logout'