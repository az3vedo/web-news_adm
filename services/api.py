from flask import request, json 

host = 'http://localhost:5101/api'

class Api:

  def getNoticias():
    url = f"{host}/noticias/"
    data = request.get(url)
    return(data.json())

  def getNoticiaById(id):
    url = f"{host}/noticias/{id}"
    data = request.get(url)
    return(data.json())

  def getAssuntos():
    url = f"{host}/assuntos/"
    data = request.get(url)
    return(data.json())
