from time import time, sleep
import os
from json import dumps
from kafka import KafkaProducer
from prometheus_client import start_http_server, Summary, Histogram, Info, Enum, Counter


KAFKA_WRITE_REQUEST_TIME = Summary('kafka_write_request_processing_seconds', 'Time spent write request to kafka')
COUNTER = Counter('requests_total', 'kafka', ['method', 'topic'])


KAFKA_SERVICE = os.getenv('KAFKA_SERVICE')
producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVICE+":9092"],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

@KAFKA_WRITE_REQUEST_TIME.time()
def kafka_write():
    current_time = time()
    data = {'datetimestamp': current_time}
    print(data, "-to "+KAFKA_SERVICE+" -")
    producer.send('input', value=data)
    COUNTER.labels('push', 'input').inc()
    sleep(5)

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        kafka_write()
