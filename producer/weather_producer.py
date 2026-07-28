from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

cities = [
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Bangalore"
]

while True:
    data = {
        "city": random.choice(cities),
        "temperature": random.randint(20, 40),
        "humidity": random.randint(40, 90)
    }

    producer.send("weather-data", data)
    print("Sent:", data)

    time.sleep(2)