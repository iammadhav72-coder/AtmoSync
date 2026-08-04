import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("sql/weather.db")
cursor = conn.cursor()

# Drop old table if it exists
cursor.execute("DROP TABLE IF EXISTS weather")

# Create new weather table
cursor.execute("""
CREATE TABLE weather (
    datetime TEXT,
    city TEXT,
    temperature INTEGER,
    humidity INTEGER,
    pressure INTEGER,
    wind_speed REAL,
    rainfall REAL,
    aqi INTEGER,
    status TEXT
)
""")

# Read CSV file
df = pd.read_csv("data/raw/weather_data.csv")

# Insert data into SQLite
df.to_sql("weather", conn, if_exists="append", index=False)
conn.commit()
conn.close()

print("✅ 3000 weather records inserted successfully into SQLite!")