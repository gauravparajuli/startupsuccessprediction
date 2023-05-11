import json
import pickle
import sklearn
import numpy as np

__markets = None
__countries = None
__status = {0: 'ACCQUIRED', 2: 'OPERATING', 1: 'CLOSED'}
__model = None


def predict_success(nRounds, investment, founded, first, last, country, market):
    caption = __status[__model.predict([[nRounds, (last-first).days, investment, (first - founded).days / 365, country, market]])[0]]
    print(caption)
    return caption


def get_markets():
    return __markets


def get_countries():
    return __countries


def load_saved_artifacts():
    global __markets
    global __countries
    global __model

    with open('./artifacts/market_mapping.json', 'r') as f:
        __markets = json.load(f)

    with open('./artifacts/country_code_mapping.json', 'r') as f:
        __countries = json.load(f)

    with open('./artifacts/lgr.pkl', 'rb') as f:
        __model = pickle.load(f)


load_saved_artifacts()

if __name__ == '__main__':
    load_saved_artifacts()
    print(__status)
    # print(get_location_names())
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    # print(get_estimated_price('Kalhalli', 1000, 2, 2))
