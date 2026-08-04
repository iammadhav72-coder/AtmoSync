import sqlite3
import pandas as pd

# Read the business dataset
df = pd.read_csv("data/raw/business_weather_data.csv")

# Connect to SQLite database
conn = sqlite3.connect("atmosync_weather.db")

# Load data into a new table
df.to_sql(
    "business_weather",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print(f"✅ {len(df)} business records inserted successfully into SQLite!")