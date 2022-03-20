from flask import Flask, render_template, request, redirect
from jinja2 import PackageLoader, Environment, select_autoescape
app = Flask(__name__)
noticias = [
            {
              "titulo": "Acidente de carro",
              "autor": "Pedro Cabral",
              "categoria": "sensacionalismo",
              "materia": "Pedro Paulo Ricardo Gabriel Maria Fabricio Fernando José Raul William Douglas Charles Beatriz Vitória Bianca"
            },
            {
              "titulo": "Ganhador da loteria",
              "autor": "João das Neves",
              "categoria": "falta do que fazer",
              "materia": "Pedro Paulo Ricardo Gabriel Maria Fabricio Fernando José Raul William Douglas Charles Beatriz Vitória Bianca"
            }
          ]

admins = [
  {
    "id" : 0,
    "nome": "Gabriel A. Souza",
    "email": "gabriel@webnews.com.br",
    "senha": "04b6e1a104ba0ed5e7985abde3e13140",
  },
  {
    "id" : 1,
    "nome": "Igor Sene",
    "email": "igor@webnews.com.br",
    "senha": "a30c6179cc93d1f26982c1d26361cb2c",
  },
  {
    "id" : 2,
    "nome": "Maria Eduarda Basilio",
    "email": "duda@webnews.com.br",
    "senha": "911396e59a692150b0217c16c3f9f046",
  }
]

def select_admin(position):
  result = list(filter(lambda x: x["id"] == position, admins))
  return result[0]

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