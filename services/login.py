from contextlib import closing
from sqlalchemy import JSON, engine_from_config
from database.db import Login
from database.engine import db_session

'''
  - Coletar os dados do cadastro
  - Coletar os dados do usuaŕio admin no banco
  - Comparar os dados e retornar o resultado
'''

class LoginService:
  
  @staticmethod
  def fetch_request(request_data):
    user_request = request_data
    return user_request

  @staticmethod
  def fetch_admin_user():
    with closing(db_session):
      query = db_session.query(Login.userName, Login.senha).one()
      header = ["userName", "senha"]
      admin_user = dict(zip(header, query))
      print("admin_user", admin_user)
      return admin_user

  def doLogin(self, request_login):
    user_login = self.fetch_request(request_login)
    admin_login = self.fetch_admin_user()
    user_match = user_login['userName'] == admin_login['userName']
    password_match = user_login['senha'] == admin_login['senha']
    return (user_match and password_match)