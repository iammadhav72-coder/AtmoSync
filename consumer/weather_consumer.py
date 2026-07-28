from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "weather-data",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Waiting for weather data...")

with open("data/raw/weather_data.json", "a") as file:
    for message in consumer:
        print("Received:", message.value)

        json.dump(message.value, file)
        file.write("\n")