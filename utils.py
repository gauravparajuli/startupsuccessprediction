import json
import pickle
# import sklearn
import numpy as np

__markets = None
__countries = None
__status = None
__model = None


def predict_success(nRounds, founded_date, first_funded_date, last_funded_date, country, market):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_markets():
    return __markets


def get_countries():
    return __countries


def load_saved_artifacts():
    global __markets
    global __countries
    global __status
    # global __model

    with open('./artifacts/market_mapping.json', 'r') as f:
        __markets = json.load(f)

    with open('./artifacts/country_code_mapping.json', 'r') as f:
        __countries = json.load(f)

    with open('./artifacts/status_mapping.json', 'r') as f:
        __status = json.load(f)

    # with open('./artifacts/banglore_home_model.pickle', 'rb') as f:
    #     __model = pickle.load(f)


load_saved_artifacts()

if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_location_names())
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    # print(get_estimated_price('Kalhalli', 1000, 2, 2))
