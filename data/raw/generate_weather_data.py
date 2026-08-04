import pandas as pd
import random
from datetime import datetime, timedelta

cities = [
    "Hyderabad", "Bengaluru", "Chennai", "Mumbai", "Delhi",
    "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Lucknow"
]

weather_status = ["Sunny", "Cloudy", "Rainy", "Storm", "Fog", "Clear"]
container_ids = [f"C{i:03}" for i in range(1, 301)]

fruits = [
    "Avocado",
    "Banana",
    "Mango",
    "Orange",
    "Apple"
]

destination_markets = [
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Bengaluru",
    "Pune"
]
rows = []

start_date = datetime(2025, 1, 1)

for i in range(3000):
    city = random.choice(cities)
    container_id = random.choice(container_ids)
    fruit = random.choice(fruits)
    destination_market = random.choice(markets)

    temperature = random.randint(18, 42)
    humidity = random.randint(25, 95)
    pressure = random.randint(980, 1035)
    wind_speed = round(random.uniform(0.5, 25.0), 1)
    rainfall = round(random.uniform(0, 120), 1)
    aqi = random.randint(30, 350)
    status = random.choice(weather_status)
# Business Logic - Spoilage Rate
if temperature <= 8:
    spoilage_rate = random.randint(1, 5)
elif temperature <= 12:
    spoilage_rate = random.randint(6, 15)
else:
    spoilage_rate = random.randint(16, 35)
    # Remaining Shelf Life
shelf_life_days = max(1, 10 - (spoilage_rate // 3))
# Risk Level
if shelf_life_days >= 7:
    risk_level = "Low"
elif shelf_life_days >= 4:
    risk_level = "Medium"
else:
    risk_level = "High"
    # Estimated Loss (₹)
if risk_level == "Low":
    estimated_loss = random.randint(5000, 15000)
elif risk_level == "Medium":
    estimated_loss = random.randint(15001, 50000)
else:
    estimated_loss = random.randint(50001, 150000)
    # Arbitrage Savings (₹)
if risk_level == "Low":
    arbitrage_savings = random.randint(1000, 5000)
elif risk_level == "Medium":
    arbitrage_savings = random.randint(5000, 20000)
else:
    arbitrage_savings = random.randint(20000, 80000)
    timestamp = start_date + timedelta(hours=i)
fruits = [
    "Avocado",
    "Banana",
    "Mango",
    "Apple",
    "Grapes"
]

container_ids = [f"C{str(i).zfill(3)}" for i in range(1,301)]

markets = [
    "Delhi",
    "Mumbai",
    "Hyderabad",
    "Bengaluru",
    "Chennai",
    "Pune",
    "Jaipur"
]
rows.append([
    timestamp.strftime("%Y-%m-%d %H:%M:%S"),
    container_id,
    fruit,
    city,
    destination_market,
    temperature,
    humidity,
    pressure,
    wind_speed,
    rainfall,
    aqi,
    status,
    spoilage_rate,
    shelf_life_days,
    risk_level,
    estimated_loss,
    arbitrage_savings
])

df = pd.DataFrame(rows, columns=[
    "datetime",
    "container_id",
    "fruit",
    "origin_city",
    "destination_market",
    "temperature",
    "humidity",
    "pressure",
    "wind_speed",
    "rainfall",
    "aqi",
    "status",
    "spoilage_rate",
    "shelf_life_days",
    "risk_level",
    "estimated_loss",
    "arbitrage_savings"
])
df.to_csv("data/raw/weather_data.csv", index=False)

print("✅ weather_data.csv created successfully!")
print(df.head())