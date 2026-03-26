import requests

class WeatherTool:
    name = "get_weather"
    description = "Fetch weather data for a given city"

    def run(self, city: str):
        API_KEY = "8cf6c18bcec0dbe76e6c378aea083590"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url)

        if res.status_code != 200:
            return {
                "error": f"API failed: {res.status_code}",
                "details": res.text
            }

        data = res.json()

        # ✅ SAFE CHECK
        if "main" not in data:
            return {"error": "Invalid response from API"}

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }