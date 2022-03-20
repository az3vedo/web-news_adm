from flask import Flask, render_template, request
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
  return render_template(template, page={'title':"Admins Control"})