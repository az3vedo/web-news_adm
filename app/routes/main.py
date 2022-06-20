from flask import Blueprint, render_template, request
from flask_login import login_required

noticias = [
            {
              "titulo": "Time da cidade passa para as semi-finais!",
              "autor": "Pedro Cabral",
              "categoria": "Esporte",
              "materia": "Pedro Paulo Ricardo Gabriel Maria Fabricio Fernando José Raul William Douglas Charles Beatriz Vitória Bianca"
            },
            {
              "titulo": "Vai chover canivetes!",
              "autor": "João das Neves",
              "categoria": "Clima e previsão do tempo",
              "materia": "Pedro Paulo Ricardo Gabriel Maria Fabricio Fernando José Raul William Douglas Charles Beatriz Vitória Bianca"
            },
            {
              "titulo": "Novo esporte domina as escolas da cidade",
              "autor": "João das Neves",
              "categoria": "Esporte",
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
  return render_template('controle_noticias.html', noticias=enumerate(noticias), page={'title':"News Control"})

@main.route('/edita_noticias')
@login_required
def news_edit():
  posicao = int(request.args['q'])
  return render_template('edita_noticias.html', noticia=noticias[posicao], page={'title':"News Edit"})

@main.route('/adiciona_noticias')
@login_required
def news_add():
  return render_template('adiciona_noticias.html', page={'title':"News Add"})
