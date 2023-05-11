from flask import Flask, request, jsonify, render_template
import os
import utils

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
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': utils.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print('Starting Flask Server for Banglore House Price prediction')
    app.run()
