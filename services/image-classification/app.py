import logging
from flask import (Flask, request)

from database.database_wrapper import DatabaseWrapper
from image_prediction.image_prediction import ImagePrediction

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

app = Flask(__name__)

database_wrapper = DatabaseWrapper()
image_prediction = ImagePrediction()


@app.route("/predict", methods=["POST"])
def classify_image():
    predicted_value = image_prediction.predict_value(request.data)
    database_wrapper.insert_prediction(predicted_value, request.data)

    return str(predicted_value)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
