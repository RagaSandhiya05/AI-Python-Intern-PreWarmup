import os

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query

load_dotenv()

GEOCODING_API_URL = os.getenv(
    "GEOCODING_API_URL",
    "https://geocoding-api.open-meteo.com/v1/search",
)
WEATHER_API_URL = os.getenv(
    "WEATHER_API_URL",
    "https://api.open-meteo.com/v1/forecast",
)
REQUEST_TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "10"))

app = FastAPI(
    title="Weather Summary API",
    description="Fetches weather data and returns a simple summary.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {"message": "Welcome to the Weather Summary API"}


@app.get("/weather")
def get_weather(city: str = Query(..., min_length=2)):
    try:
        with httpx.Client(timeout=REQUEST_TIMEOUT) as client:
            # Find the city's coordinates.
            geo_response = client.get(
                GEOCODING_API_URL,
                params={"name": city, "count": 1},
            )
            geo_response.raise_for_status()
            locations = geo_response.json().get("results", [])

            if not locations:
                raise HTTPException(
                    status_code=404,
                    detail="City not found",
                )

            location = locations[0]

            # Fetch weather data for the coordinates.
            weather_response = client.get(
                WEATHER_API_URL,
                params={
                    "latitude": location["latitude"],
                    "longitude": location["longitude"],
                    "current": (
                        "temperature_2m,"
                        "relative_humidity_2m,"
                        "apparent_temperature,"
                        "wind_speed_10m"
                    ),
                    "hourly": "temperature_2m",
                    "forecast_days": 1,
                    "timezone": "auto",
                },
            )
            weather_response.raise_for_status()
            weather_data = weather_response.json()

        current = weather_data["current"]
        temperatures = weather_data["hourly"]["temperature_2m"][:6]
        valid_temperatures = [
            temperature
            for temperature in temperatures
            if temperature is not None
        ]

        average_temperature = (
            round(sum(valid_temperatures) / len(valid_temperatures), 2)
            if valid_temperatures
            else None
        )

        return {
            "city": location["name"],
            "country": location.get("country"),
            "current_temperature_c": current["temperature_2m"],
            "feels_like_c": current["apparent_temperature"],
            "humidity_percent": current["relative_humidity_2m"],
            "wind_speed_kmh": current["wind_speed_10m"],
            "next_6_hours_average_temperature_c": average_temperature,
            "temperature_summary": (
                "Warmer conditions"
                if average_temperature is not None
                and average_temperature > current["temperature_2m"]
                else "Similar or cooler conditions"
            ),
            "timezone": weather_data.get("timezone"),
        }

    except HTTPException:
        raise
    except httpx.HTTPError as error:
        raise HTTPException(
            status_code=502,
            detail="Unable to retrieve weather data from the external API",
        ) from error
    except (KeyError, TypeError, ValueError):
        raise HTTPException(
            status_code=502,
            detail="Received unexpected data from the weather API",
        )
