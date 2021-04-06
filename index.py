

#!/usr/bin/env python3

from collections import OrderedDict
import flask
from flask import Flask, request, Response, jsonify, render_template 
import urllib.parse
import requests
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.config['DEBUG'] = False
port = 83
key = "7e6b9ffa10bb2e7c20ce93d7e263454f"

CORS(app, resources=r'/api/*')
@app.route('/', methods=['get'])
def index():

    # -----------------------------------------------
    # Welcome
    # -----------------------------------------------
    return jsonify({"mensagem": "Acesso via /api"})

@app.route('/api/weather/city/', methods=['GET'])
def weatherByCity():

    # -----------------------------------------------
    # Example request GET
    # /api/weather/city/?city=Belo%20Horizonte,minas%20gerais
    # -----------------------------------------------

    city = urllib.parse.quote(request.args['city']) #""

    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&lang=pt_br&units=metric&cnt=50&APPID="+key
    response = requests.get(url)

    return Response(response)  

@app.route('/api/weather', methods=['GET'])
def weatherByLatLong():

    # -----------------------------------------------
    # Example request GET
    # /api/weather?lat=-19.8218131&lon=-44.0094874
    # -----------------------------------------------

    lat = urllib.parse.quote(request.args['lat']) #""
    lon = urllib.parse.quote(request.args['lon']) #""

    url = "http://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&lang=pt_br&units=metric&cnt=50&APPID="+key
    response = requests.get(url)

    return Response(response)  

app.run(host="0.0.0.0", port=port)
