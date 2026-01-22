
import json
import psycopg2
from kafka import KafkaConsumer

conn = psycopg2.connect(
    dbname="weatherdb",
    user="user",
    password="password",
    host="postgres",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS weather_data (
    time TEXT,
    temperature FLOAT,
    windspeed FLOAT
)
""")
conn.commit()

consumer = KafkaConsumer(
    "weather-topic",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

for message in consumer:
    data = message.value
    cur.execute(
        "INSERT INTO weather_data VALUES (%s, %s, %s)",
        (data.get("time"), data.get("temperature"), data.get("windspeed"))
    )
    conn.commit()
    print("Stored:", data)
