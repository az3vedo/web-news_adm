from flask import Blueprint, render_template, request
from flask_login import login_required
from jinja2 import PackageLoader, Environment, select_autoescape
from app.services.api import Api

main = Blueprint('main', __name__)

@main.route('/')
def index():
  return render_template('login.html', page={'title': "Web News Admin"})

# @main.route('/home')
# @login_required
# def home():
#   return render_template('home.html', page={'title': "Web News Admin"})

@main.route('/controle_noticias')
@login_required
def news_control():
  return render_template('controle_noticias.html', page={'title':"News Control"}, noticias=Api.getNoticias())

@main.route('/edita_noticias/<id>')
@login_required
def news_edit(id):
  return render_template('edita_noticias.html', page={'title':"News Edit"}, noticia=Api.getNoticiaById(id))

@main.route('/adiciona_noticias')
@login_required
def news_add():
  return render_template('adiciona_noticias.html', page={'title':"News Add"})

@main.route('/adiciona_assunto')
@login_required
def assunto_add():
  return render_template('adiciona_assuntos.html', page={'title':"Add Assunto"})

@main.route('/adiciona_autor')
@login_required
def autor_add():
  return render_template('adiciona_autores.html', page={'title':"Add Autor"})