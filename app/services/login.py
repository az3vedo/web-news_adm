from app.models import Login
from flask_login import login_user

'''
  - Coletar os dados do cadastro
  - Coletar os dados do usuaŕio admin no banco
  - Comparar os dados e retornar o resultado
'''

class LoginService:

  @staticmethod
  def get_admin_user():
    query = Login.query.filter_by(userName='admin').first()
    return query
  
  @staticmethod
  def fetch_request(request_data):
    user_request = request_data
    return user_request

  @staticmethod
  def fetch_admin_user():
    admin_user = Login.query.filter_by(userName='admin').first()
    return admin_user

  def doLogin(self, request_login):
    user_login = self.fetch_request(request_login)
    admin_login = self.fetch_admin_user()
    user_match = user_login['userName'] == admin_login.userName
    password_match = user_login['senha'] == admin_login.senha
    login_match =  (user_match and password_match)
    if (login_match):
      login_user(self.get_admin_user(), remember=True)
    return login_match