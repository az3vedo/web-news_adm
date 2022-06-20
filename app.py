from flask import Flask, render_template, request, redirect
from jinja2 import PackageLoader, Environment, select_autoescape
from services.api import Api

app = Flask(__name__)

env = Environment(
  loader=PackageLoader("app"),
  autoescape=select_autoescape()
)

@app.route('/')
def home():
  template = env.get_template('login.html')
  return render_template(template, page={'title':"Admin Login"})

@app.route('/controle_noticias')
def news_control():
  noticias = Api.getNoticias()
  template = env.get_template('controle_noticias.html')
  return render_template(template, noticias=enumerate(noticias), page={'title':"News Control"})

@app.route('/edita_noticias')
def news_edit():
  template = env.get_template('edita_noticias.html')
  posicao = int(request.args['q'])
  return render_template(template, noticia=noticias[posicao], page={'title':"News Edit"})

@app.route('/adiciona_noticias')
def news_add():
  template = env.get_template('adiciona_noticias.html')
  return render_template(template, page={'title':"News Add"})

@app.route('/adiciona_assunto')
def assunto_add():
  template = env.get_template('adiciona_assunto.html')
  return render_template(template, page={'title':"Add Assunto"})

@app.route('/adiciona_autor')
def autor_add():
  template = env.get_template('adiciona_autor.html')
  return render_template(template, page={'title':"Add Autor"})

@app.route('/controle_admins')
def admins_control():
  template = env.get_template('controle_admins.html')
  return render_template(template,admins=enumerate(admins), page={'title':"Admins Control"})

@app.route('/edita_admins')
def admins_edit():
  template = env.get_template('edita_admins.html')
  posicao = int(request.args['q'])
  return render_template(template,admin=admins[posicao], page={'title':"Admins Update"})

@app.route('/altera_senha')
def passwd_edit():
  template = env.get_template('altera_senha.html')
  posicao = int(request.args['q'])
  return render_template(template,admin=select_admin(posicao), page={'title':"Password Update"})