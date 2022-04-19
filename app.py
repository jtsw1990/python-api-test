'''
from flask import Flask, jsonify, request
from statsmodels.iolib.smpickle import load_pickle
import numpy as np
import json

app = Flask(__name__)
loaded_model = load_pickle("model/claims_model.pickle")
model_schema = {
    "age": "integer",
    "bmi": "float",
    "children": "integer",
    "sex_female": "integer",
    "sex_male": "integer",
    "smoker_no": "integer",
    "smoker_yes": "integer",
    "region_northeast": "integer",
    "region_northwest": "integer",
    "region_southeast": "integer",
    "region_southwest": "integer",
}


@app.route("/", methods=["GET"])
def get_schema():
    return jsonify(model_schema)


@app.route("/", methods=["POST"])
def get_claims():
    record = json.loads(request.data)
    result = {}
    for key, value in model_schema.items():
        result[key] = record[key]
    result_formatted = np.array([x[-1] for x in list(result.items())])
    predicted_claims = loaded_model.predict(result_formatted)
    return jsonify({"claims_cost": predicted_claims[0]})
'''

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Medium"



if __name__ == "__main__":
    app.run(port=5000, debug=True)
