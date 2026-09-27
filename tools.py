import requests

def get_weather(lat: float, lon: float) -> dict:
    """Returns the current weather at a location in Toronto"""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current": "temperature_2m,precipitation,weather_code"}
    data = requests.get(url, params=params, timeout=10).json()
    return data["current"]

if __name__ == "__main__":
    #Union Station
    print(get_weather(43.6453, -79.3806))