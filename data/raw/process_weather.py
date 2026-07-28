import json

input_file = "processed/weather_data.json"
output_file = "processed/processed_weather.json"

processed_data = []

with open(input_file, "r") as f:
    for line in f:
        item = json.loads(line)

        item["status"] = "Hot" if item["temperature"] > 30 else "Normal"

        processed_data.append(item)

with open(output_file, "w") as f:
    json.dump(processed_data, f, indent=4)

print("Processed data saved successfully!")