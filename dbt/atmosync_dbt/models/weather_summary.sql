SELECT
    city,
    AVG(temperature) AS avg_temperature,
    AVG(humidity) AS avg_humidity
FROM main.weather
GROUP BY city;