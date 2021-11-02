from time import time, sleep
import os
import rfc3339
import iso8601
import json
from json import dumps, loads
from kafka import KafkaProducer, KafkaConsumer
from prometheus_client import start_http_server, Summary, Histogram, Info, Enum, Counter

KAFKA_SERVICE = os.getenv('KAFKA_SERVICE')

COUNTER = Counter('requests_total', 'kafka', ['method', 'topic'])

consumer = KafkaConsumer(
    'input',
     bootstrap_servers=[KAFKA_SERVICE+":9092"],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='cons_test',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVICE+":9092"],
     value_serializer=lambda x:
     dumps(x).encode('utf-8'))

def kafka_read_write():
    for message in consumer:
        message = message.value
        print(message, "-original")
        COUNTER.labels('pull', 'input').inc()
        message["datetimestamp"] = rfc3339.rfc3339(message["datetimestamp"])
        print(message, "-transformed")
        producer.send('output', value=message)
        COUNTER.labels('push', 'output').inc()

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        kafka_read_write()
