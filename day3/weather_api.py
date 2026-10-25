import requests

API_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_PARAMETERS = {
    "latitude": 11.0168,
    "longitude": 76.9558,
    "current": (
        "temperature_2m,"
        "relative_humidity_2m,"
        "apparent_temperature,"
        "wind_speed_10m"
    ),
}


def get_weather():
    """Fetch current weather data from the Open-Meteo API."""

    try:
        response = requests.get(
            API_URL,
            params=WEATHER_PARAMETERS,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()
        current = data["current"]
        units = data["current_units"]

        print("\n========== WEATHER REPORT ==========")
        print("Location: Coimbatore")
        print(f"Time: {current['time']}")

        print(
            f"Temperature: {current['temperature_2m']} "
            f"{units['temperature_2m']}"
        )

        print(
            f"Feels Like: {current['apparent_temperature']} "
            f"{units['apparent_temperature']}"
        )

        print(
            f"Humidity: {current['relative_humidity_2m']} "
            f"{units['relative_humidity_2m']}"
        )

        print(
            f"Wind Speed: {current['wind_speed_10m']} "
            f"{units['wind_speed_10m']}"
        )

        print("====================================")

    except requests.exceptions.Timeout:
        print("Error: The API request timed out.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Network Error: {error}")

    except (KeyError, ValueError) as error:
        print(f"Error processing the API response: {error}")


if __name__ == "__main__":
    get_weather()
