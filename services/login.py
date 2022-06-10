from contextlib import closing
from flask import Flask

from database.db import Login
from database.engine import db_session

'''
    - Pegar o login do banco
    - Comparar com o login do request
    - Retorna se o login é válido
'''

def fetch_login():
    with closing(db_session):
        admin_user = db_session.query(Login.userName, Login.senha).filter(id=1).one()
    return admin_user

def compareLogin(request_login, admin_login=fetch_login()):
    username_match = request_login['userName'] and admin_login['userName']
    password_match = request_login['senha'] and admin_login['senha']
    return (username_match and password_match)

def doLogin(login):
    return compareLogin(login)
