import sqlite3
import json

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    city TEXT,
    temperature INTEGER,
    humidity INTEGER,
    status TEXT
)
""")

with open("../data/raw/processed/processed_weather.json", "r") as f:
    data = json.load(f)

for row in data:
    cursor.execute("""
    INSERT INTO weather VALUES (?, ?, ?, ?)
    """, (
        row["city"],
        row["temperature"],
        row["humidity"],
        row["status"]
    ))

conn.commit()

print("Data inserted successfully!")

conn.close()