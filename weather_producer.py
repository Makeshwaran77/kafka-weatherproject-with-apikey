
import json
import time
import requests
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true"

while True:
    response = requests.get(API_URL).json()
    weather = response.get("current_weather", {})
    producer.send("weather-topic", weather)
    print("Sent:", weather)
    time.sleep(10)
