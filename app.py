import flask
import requests 
from flask import Flask, render_template, request


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "Welcome to the starting page"


@app.route('/input/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        lattitude = request.form.get('lattitude')  # access the data inside 
        longitude = request.form.get('longitude')

        url = 'https://europe-west1-freesolarcalc.cloudfunctions.net/wave_max/'
        params = {"lat":float(lattitude), "lon":float(longitude)}
        res = requests.get(url, params)
        message = res.text
    return render_template('input.html', message=message)
#...


app.run()
