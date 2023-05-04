import pandas as pd
import numpy as np

import pickle
import json

def read_from_json(file_handle: str) -> dict:
    with open(file_handle, "r") as open_file:
        json_object = json.load(open_file)
    return json_object

def combine_model_name(model_name: str) -> str:
    model_name_list = model_name.split(" ")
    return "-".join(model_name_list)


MODEL_FILEPATH = "../ml_models/model_file.pkl"
FEATURE_STORE_FILEPATH = "../ml_models/model_feature_store.json"

def predict_price(input_data: dict) -> dict:
    # load the model - move this to dockerfile to load on run
    restored_model = pickle.load(open(MODEL_FILEPATH, "rb"))

    # load feature store - move this to dockerfile to load on run
    feature_store_dict = read_from_json(file_handle=FEATURE_STORE_FILEPATH)
    feature_list = feature_store_dict.get("feature_list")

    input_df = pd.DataFrame(0, index=np.arange(1), columns=feature_list)

    # add sample data to sparse input vector
    new_sample = {
        "year": input_data["year"],
        "manufacturer": input_data["manufacturer"].lower(),
        "model": input_data["model"].lower(),
        "paint_color": input_data["color"].lower()
    }

    new_dict = {}
    for key, value in new_sample.items():
        if key == "model":
            value = combine_model_name(model_name=value)
        feature_name = f"{key}_{str(value)}"
        new_dict[feature_name] = value

    # add a 1 to the columns with the same names as the keys
    for k, v in new_dict.items():
        if k in feature_list:
            input_df.at[0, k] = 1
        else:
            print(f"{k} not in feature list")

    # predict the price
    prediction = restored_model.predict(input_df)

    # send a json response or store in database
    price_pred = round(prediction[0], 2)

    output_dict = input_data["suggested_price"] = price_pred
    return output_dict
