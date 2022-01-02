import logging
import requests
from flask import (Flask, request)

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

app = Flask(__name__)

url = "http://image-classification.default.svc.cluster.local:8080/predict"


@app.route("/predict", methods=["POST"])
def classify_image():
    response = requests.post(url=url, data=request.data)

    if response.ok:
        logging.info("Image successfully predicted!")
        return response.text
    else:
        logging.info("Failed to predict image!")
        logging.error(str(response.status_code) + ": " + response.text)
        return response.text, response.status_code


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
