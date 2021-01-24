#!/usr/bin/env python3
import json
import time

import requests
from confluent_kafka import Producer

p = Producer({"bootstrap.servers": "localhost:9092"})

req = requests.get("https://api.tfl.gov.uk/line/207/arrivals/")
for row in req.json():
    print(row['expectedArrival'] + " - " + row['stationName'])

    p.produce("bus209", key=row['stationName'], value=json.dumps(row))
    time.sleep(0.1)
