from datetime import date
from flask import Flask, request, jsonify, render_template
import os
import utils
import datetime

app = Flask(__name__, template_folder='client',
            static_folder='client', static_url_path='/static')


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'Hi!'


@app.route('/get_markets')
def get_markets():
    response = jsonify({
        'markets': utils.get_markets()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_countries')
def get_countries():
    response = jsonify({
        'countries': utils.get_countries()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/estimate', methods=['POST'])
def estimate_house_price():
    nRounds = float(request.form['nRounds'])
    investment = float(request.form['investment'])
    founded = datetime.datetime.strptime(
        request.form['founded'], '%m/%d/%Y')
    first = datetime.datetime.strptime(
        request.form['first'], '%m/%d/%Y')
    last = datetime.datetime.strptime(request.form['last'], '%m/%d/%Y')
    # market = utils.get_markets()[request.form['market']]
    # country = utils.get_markets()[request.form['country']]
    market = request.form['market']
    country = request.form['country']

    response = jsonify({
        'status': utils.predict_success(nRounds, investment, founded, first, last, market, country)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print('Starting Flask Server for Banglore House Price prediction')
    app.run()
