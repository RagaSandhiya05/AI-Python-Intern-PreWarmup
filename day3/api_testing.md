# T13 — API Testing with Postman and cURL

## Objective

To test HTTP requests independently using Postman or cURL, inspect response headers and JSON bodies, and understand successful and unsuccessful HTTP responses.

## Tools Used

- Postman or cURL
- Open-Meteo public weather API
- httpbin HTTP testing service

## Test Cases

### 1. GET Request — Weather API

- **Method:** GET
- **Endpoint:** `https://api.open-meteo.com/v1/forecast`
- **Purpose:** Retrieve current weather information.
- **Parameters:** Latitude, longitude, and requested weather fields.
- **Expected result:** Successful HTTP response containing weather data in JSON format.

### 2. POST Request — httpbin

- **Method:** POST
- **Endpoint:** `https://httpbin.org/post`
- **Purpose:** Submit a JSON request body and inspect the server's response.
- **Request format:** JSON
- **Expected result:** Successful response containing the submitted JSON and request headers.

### 3. Error Response — httpbin

- **Method:** GET
- **Endpoint:** `https://httpbin.org/status/404`
- **Purpose:** Test how an API returns an unsuccessful HTTP response.
- **Expected result:** HTTP 404 Not Found.

## Request and Response Comparison

| Feature | Python Requests | Postman / cURL |
|---|---|---|
| Request methods | Supported | Supported |
| Query parameters | Supported | Supported |
| Request headers | Supported | Supported |
| JSON body | Supported | Supported |
| Status codes | Accessible in code | Displayed in the response |
| Response headers | Accessible in code | Visible in the response |

## Key Learnings

1. GET requests retrieve information from an API.
2. POST requests can submit structured data in a JSON body.
3. HTTP headers provide additional information about requests and responses.
4. Status codes help identify successful requests and errors.
5. Postman and cURL allow API testing without writing a dedicated Python program.
6. API responses should be checked and handled appropriately in application code.

## Evidence

The following screenshots demonstrate the completed test cases:

- `screenshots/01_get_weather.png`
- `screenshots/02_post_request.png`
- `screenshots/03_error_response.png`

## Conclusion

This task provided practical experience in sending GET and POST requests, inspecting HTTP response headers and JSON bodies, and testing an intentional 404 response. These skills are useful when debugging and integrating APIs into Python applications.