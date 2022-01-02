FROM tensorflow/tensorflow:2.7.0

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py /app/app.py
COPY database/ /app/database
COPY image_prediction/ /app/image_prediction

CMD [ "python3", "app.py"]