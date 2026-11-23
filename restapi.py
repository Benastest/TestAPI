import requests

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=52.2799"
    "&longitude=8.0472"
    "&daily=temperature_2m_max,temperature_2m_min"
    "&timezone=Europe/Berlin"
)

response = requests.get(url)

daten = response.json()

datum = daten["daily"]["time"][0]
max_temperatur = daten["daily"]["temperature_2m_max"][0]
min_temperatur = daten["daily"]["temperature_2m_min"][0]


# temperatur = daten["current"]["temperature_2m"]

print(f"Aktuelles Datum: {datum}")
print(f"Maximale Temperatur in Osnabrück: {max_temperatur}°C")
print(f"Minimale Temperatur in Osnabrück: {min_temperatur}°C")