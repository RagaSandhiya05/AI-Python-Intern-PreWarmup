# Weather Summary API

A containerized REST API built using **FastAPI** that retrieves weather information for a given city, processes the data, and returns a structured JSON response. The application integrates with the Open-Meteo Geocoding API and Weather Forecast API to fetch location and weather information.

This project demonstrates Python API development, HTTP requests, environment-based configuration, error handling, API testing, and Docker containerization.

## System Architecture

<img width="1104" height="2450" alt="mermaid-diagram (6)" src="https://github.com/user-attachments/assets/a69f4ac9-7b03-4b4c-b2d5-f961c71e49e0" />

## Features

- **City-based Weather Search:** Retrieve weather information using a city name.
- **External API Integration:** Fetch geographical coordinates and weather data using Open-Meteo.
- **Weather Data Processing:** Calculate the average temperature over the next six hourly forecast values.
- **Structured JSON Responses:** Return relevant weather information in a clean JSON format.
- **Error Handling:** Handle unknown cities, external API failures, and unexpected response data.
- **Environment Configuration:** Configure API endpoints and request timeouts using environment variables.
- **Interactive API Documentation:** Explore and test endpoints through FastAPI's Swagger UI.
- **Docker Support:** Build and run the application inside a Docker container.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| FastAPI | REST API framework |
| HTTPX | HTTP requests to external APIs |
| Uvicorn | ASGI server |
| python-dotenv | Load environment variables |
| Open-Meteo | Geocoding and weather data |
| Docker | Application containerization |
| Git and GitHub | Version control and source management |

## Project Structure

```text
day5/capstone/
├── main.py
├── requirements.txt
├── Dockerfile
├── .env
├── .dockerignore
├── README.md
└── screenshots/
    ├── 01_home_endpoint.png
    ├── 02_weather_api_response.png
    ├── 03_swagger_ui.png
    ├── 04_unknown_city_error.png
    ├── 05_docker_image_build.png
    ├── 06_docker_container_running.png
    └── 07_containerized_api_response.png
```

**Note:** The `.env` file contains local configuration and should not be committed to GitHub. The `.dockerignore` file prevents it from being copied into the Docker image.

## Prerequisites

Ensure the following are installed:

- Python 3.10 or later
- pip
- Docker Desktop
- Git
- A web browser
- An active internet connection

## Installation and Setup

### 1. Clone the repository

If you have not already cloned the repository, run:

```bash
git clone https://github.com/RagaSandhiya05/AI-Python-Intern-PreWarmup.git
cd AI-Python-Intern-PreWarmup
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

From the repository root:

```powershell
python -m pip install -r day5/capstone/requirements.txt
```

### 4. Configure environment variables

Create a `.env` file inside `day5/capstone/` with the following configuration:

```dotenv
GEOCODING_API_URL=https://geocoding-api.open-meteo.com/v1/search
WEATHER_API_URL=https://api.open-meteo.com/v1/forecast
REQUEST_TIMEOUT=10
```

These variables configure the external API endpoints and the HTTP request timeout.

The application uses default values for these settings if the corresponding environment variables are not defined.

## Running the Application Locally

Start the FastAPI application from the repository root:

```powershell
python -m uvicorn main:app --app-dir day5/capstone --reload
```

The server will be available at:

```text
http://127.0.0.1:8000
```

The `--reload` option automatically restarts the server when the source code changes.

## API Endpoints

### 1. Home Endpoint

**Method:** `GET`

**URL:** `/`

Returns a welcome message to confirm that the API is running.

Example request:

```http
GET /
```

Example response:

```json
{
  "message": "Welcome to the Weather Summary API"
}
```

### 2. Weather Summary Endpoint

**Method:** `GET`

**URL:** `/weather`

**Query parameter:** `city` — the name of the city to search for.

Example request:

```http
GET /weather?city=Coimbatore
```

Example browser URL:

```text
http://127.0.0.1:8000/weather?city=Coimbatore
```

Example response structure:

```json
{
  "city": "Coimbatore",
  "country": "India",
  "current_temperature_c": 29.5,
  "feels_like_c": 32.1,
  "humidity_percent": 65,
  "wind_speed_kmh": 12.4,
  "next_6_hours_average_temperature_c": 29.8,
  "temperature_summary": "Warmer conditions",
  "timezone": "Asia/Kolkata"
}
```

*The values above are illustrative. Actual results depend on the weather data returned by Open-Meteo.*

### Response Fields

| Field | Description |
|---|---|
| `city` | Name of the matched city |
| `country` | Country associated with the location |
| `current_temperature_c` | Current temperature in Celsius |
| `feels_like_c` | Apparent temperature in Celsius |
| `humidity_percent` | Relative humidity percentage |
| `wind_speed_kmh` | Wind speed in kilometres per hour |
| `next_6_hours_average_temperature_c` | Average of the available temperature forecast values among the next six hourly entries |
| `temperature_summary` | Simple comparison between the average forecast temperature and current temperature |
| `timezone` | Time zone associated with the weather forecast |

### 3. Interactive API Documentation

FastAPI automatically generates interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Use the Swagger UI interface to inspect the endpoints, enter query parameters, execute requests, and view responses.

## Error Handling

The application handles common errors encountered while communicating with external services.

| Status code | Scenario | Example response |
|---|---|---|
| `200 OK` | Successful request | Weather information returned as JSON |
| `404 Not Found` | City not found | `{"detail": "City not found"}` |
| `422 Unprocessable Entity` | Invalid or missing query parameter | FastAPI validation error |
| `502 Bad Gateway` | External API failure or unexpected response data | Error details returned as JSON |

Example request for an unknown city:

```text
http://127.0.0.1:8000/weather?city=XYZUnknownCity999
```

Expected response:

```json
{
  "detail": "City not found"
}
```

The `502` responses help indicate that the application could not successfully process data from the external weather services.

## Docker Containerization

The application includes a Dockerfile to package the API and its Python dependencies into a container.

### 1. Build the Docker image

Run the following command from the repository root:

```powershell
docker build -t weather-summary-api:1.0 ./day5/capstone
```

This builds the image using the Dockerfile in the capstone directory.

### 2. Run the Docker container

Make sure port `8000` is available. Then run:

```powershell
docker run -d --env-file day5/capstone/.env -p 8000:8000 --name weather-api weather-summary-api:1.0
```

This command:

- Runs the container in detached mode.
- Loads the environment variables from `.env`.
- Maps host port `8000` to container port `8000`.
- Assigns the container the name `weather-api`.

### 3. Verify the running container

```powershell
docker ps
```

The output should list `weather-api` with a running status.

### 4. View container logs

```powershell
docker logs weather-api
```

The logs should contain a message similar to:

```text
Uvicorn running on http://0.0.0.0:8000
```

### 5. Test the containerized API

After starting the container, open the following URLs:

**Home endpoint**

```text
http://127.0.0.1:8000/
```

**Weather endpoint**

```text
http://127.0.0.1:8000/weather?city=Coimbatore
```

**Swagger UI**

```text
http://127.0.0.1:8000/docs
```

The containerized application should return the same types of responses as the locally running application.

### 6. Stop and remove the container

To stop the running container:

```powershell
docker stop weather-api
```

To remove the stopped container:

```powershell
docker rm weather-api
```

The Docker image remains available after removing the container. You can create a new container from the existing image when needed.

## Screenshots and Testing Evidence

The following screenshots document the implementation and testing process.

| Screenshot | Evidence |
|---|---|
| `01_home_endpoint.png` | Successful home endpoint response |
| `02_weather_api_response.png` | Weather data returned as JSON |
| `03_swagger_ui.png` | FastAPI interactive documentation |
| `04_unknown_city_error.png` | Error handling for an unknown city |
| `05_docker_image_build.png` | Successful Docker image build |
| `06_docker_container_running.png` | Uvicorn running inside the Docker container |
| `07_containerized_api_response.png` | Successful weather response from the containerized API |

The screenshots are stored in the `screenshots/` directory.

## Troubleshooting

### Port 8000 is already in use

Stop the existing local server using `Ctrl + C`, or stop the container using:

```powershell
docker stop weather-api
```

Ensure that only the intended service is using port `8000`.

### Container name already exists

If Docker reports that the container name `weather-api` is already in use, restart the existing container:

```powershell
docker start weather-api
```

If you intentionally want to recreate it, stop and remove it first:

```powershell
docker rm -f weather-api
```

Then run the `docker run` command again.

### Weather request fails

Check your internet connection, verify that the Open-Meteo services are accessible, and inspect the application logs.

For a containerized application:

```powershell
docker logs weather-api
```

### Environment variables are not loaded

Verify that `day5/capstone/.env` exists and contains the correct variable names. When using Docker, ensure the `--env-file` option points to the correct file.

## Security and Configuration Notes

- Do not commit `.env` files containing local configuration or secrets.
- Keep `.env` excluded through `.gitignore` and `.dockerignore`.
- No Open-Meteo API key is required for basic non-commercial use under its applicable terms.
- The application uses a request timeout to avoid waiting indefinitely for external responses.
- The API depends on internet access and the availability of the external weather services.

## Learning Outcomes

Through this project, I practised:

- Building REST API endpoints with FastAPI.
- Sending HTTP requests using HTTPX.
- Integrating third-party APIs.
- Processing JSON data and calculating a simple temperature summary.
- Implementing query parameter validation and error handling.
- Managing application configuration with environment variables.
- Testing API endpoints using a browser and Swagger UI.
- Creating Docker images and running containers.
- Documenting implementation and testing evidence.

## Conclusion

The Weather Summary API demonstrates the development of a Python-based REST service that integrates external weather data, processes the results, and returns structured JSON responses. Docker containerization makes the application easier to run in a consistent environment, while FastAPI's interactive documentation simplifies endpoint testing.

This project provided practical experience in API development, external service integration, configuration management, error handling, testing, and containerization.
