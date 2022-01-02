import psycopg2
import psycopg2.extras
import uuid
from datetime import datetime

dns = "dbname=postgres user=postgres password=password host=postgresql-postgresql-0.postgresql-headless.postgresql.svc.cluster.local"


class DatabaseWrapper:

    def __init__(self) -> None:
        psycopg2.extras.register_uuid()
        self.connetion = psycopg2.connect(dns)

    def insert_prediction(self, predicted_value, image):
        cur = self.connetion.cursor()
        log_id = uuid.uuid4()

        cur.execute("INSERT INTO image_classification.log (id, created_at, prediction) VALUES (%s, %s, %s)",
                    (log_id, datetime.now(), predicted_value.item()))
        cur.execute("INSERT INTO image_classification.input (id, log_id, image) VALUES (%s, %s, %s)",
                    (uuid.uuid4(), log_id, image))
        self.connetion.commit()

        cur.close()
