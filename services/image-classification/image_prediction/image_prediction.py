from numpy import argmax
from keras.preprocessing.image import img_to_array
from keras.models import load_model

from PIL import Image
import io


class ImagePrediction:

    def __init__(self) -> None:
        self.model = load_model("image_prediction/model.h5")

    def predict_value(self, bytes):
        img = self.convert_to_image(bytes)
        return argmax(self.model.predict(img))

    def convert_to_image(self, bytes):
        img = Image.open(io.BytesIO(bytes))
        img = img.resize((28, 28))
        img = img.convert("L")
        img = img_to_array(img)
        img = img.reshape(1, 28, 28, 1)
        img = img.astype("float32")
        img = img / 255.0
        return img
