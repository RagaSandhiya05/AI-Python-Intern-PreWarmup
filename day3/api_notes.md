# T11 — HTTP & REST API Concepts

## 1. Introduction to APIs

### What is an API?

API stands for **Application Programming Interface**. It is a set of rules and protocols that allows two software applications to communicate and exchange information.

An API acts as an intermediary between a client and a service. Instead of accessing another application's internal implementation, a client can request specific functionality or data through the API.

### Real-World Example

Consider a weather application. When a user searches for the weather in Coimbatore:

1. The user enters the city name in the application.
2. The application sends a request to a weather API.
3. The weather server processes the request.
4. The server returns weather information.
5. The application displays the temperature, humidity, and weather conditions.

The application does not need to maintain its own weather-measurement infrastructure. It can retrieve the required information through an API.

### Why Are APIs Important?

- Enable communication between different software applications.
- Allow developers to reuse existing services and functionality.
- Support integration between frontend applications and backend servers.
- Provide access to external services such as maps, payments, and weather data.
- Enable AI applications to communicate with machine learning models and language model services.
- Reduce development time by avoiding unnecessary duplication of functionality.

### Common Types of APIs

**1. REST APIs:** Use HTTP methods and resource-based URLs to access or modify data.

**2. SOAP APIs:** Use a structured messaging protocol, commonly with XML, for exchanging information between applications.

**3. GraphQL APIs:** Allow clients to request specific fields of data through a query language.

**4. WebSocket APIs:** Support persistent, two-way communication between clients and servers.

**5. Library APIs:** Provide functions, classes, and methods that developers can use within a programming language.

REST APIs are particularly important in Python backend development and AI application integration.

---

## 2. What Is HTTP?

HTTP stands for **Hypertext Transfer Protocol**. It is an application-layer protocol used to exchange information between clients and servers.

A client sends an HTTP request, and the server returns an HTTP response.

### How HTTP Works

1. The client identifies the resource it wants to access.
2. The client sends an HTTP request to the server.
3. The server receives and processes the request.
4. The server generates an appropriate response.
5. The client receives the response and handles the result.

For example, a Python application may request a list of products from a web server. The server returns the product data, often in JSON format.

### HTTP vs HTTPS

**HTTP:** Transfers data without the transport encryption provided by TLS.

**HTTPS:** Uses TLS to encrypt communication between the client and server, helping protect data from interception and tampering.

HTTPS should be used for applications that exchange credentials, API keys, personal information, or other sensitive data.

### Important HTTP Characteristics

- HTTP follows a request-response communication model.
- It supports different methods, such as GET, POST, PUT, and DELETE.
- Responses contain status codes that indicate the result of a request.
- Headers carry additional information about requests and responses.
- HTTP is stateless at the protocol level: each request is interpreted independently unless the application uses mechanisms such as cookies, tokens, or server-side sessions to maintain context.

---

## 3. What Is REST?

REST stands for **Representational State Transfer**. It is an architectural style for designing networked applications and web APIs.

REST APIs commonly use HTTP methods to interact with resources identified by URLs.

A resource can represent a user, product, order, student, or any other entity managed by an application.

### Example

Suppose an application manages student records.

- `GET /students` — Retrieve the collection of students.
- `GET /students/101` — Retrieve the student with ID 101.
- `POST /students` — Create a student.
- `PUT /students/101` — Replace the student resource.
- `PATCH /students/101` — Update selected fields.
- `DELETE /students/101` — Delete the student resource.

The server determines how each request is processed and what response should be returned.

### Key Principles of REST

**1. Client-server architecture**

The client handles the user interface or request logic, while the server handles application processing and data access. Separating these responsibilities improves maintainability.

**2. Statelessness**

Each request must contain the information needed to process it. The server does not rely on stored conversational request context to interpret a request, although applications may still maintain user sessions or other state through explicit mechanisms.

**3. Cacheability**

Responses should indicate whether they can be cached. Appropriate caching can reduce repeated requests and improve performance.

**4. Uniform interface**

Resources are accessed through a consistent interface, commonly using HTTP methods and resource representations such as JSON.

**5. Layered system**

A client may communicate through intermediaries such as proxies, gateways, or load balancers without needing to understand the complete server architecture.

**6. Code on demand (optional)**

A server may optionally provide executable code to a client. This is not required for a REST API.

### REST vs RESTful API

A RESTful API is an API designed to follow REST architectural constraints. In everyday development, the term REST API is often used more broadly for HTTP APIs that use resource-oriented URLs and standard HTTP methods.

---

## 4. Understanding URLs and Endpoints

A URL stands for **Uniform Resource Locator**. It identifies the address of a resource.

An API endpoint is a particular address and method combination through which an API exposes functionality or a resource.

### Example URL

`https://api.example.com/v1/students/101?include=grades`

Its components are:

- **Scheme:** `https` — specifies the protocol.
- **Host:** `api.example.com` — identifies the server.
- **Path:** `/v1/students/101` — identifies the requested resource.
- **Version:** `v1` — commonly indicates the API version in this example.
- **Query parameter:** `include=grades` — provides additional request information.

The `v1` portion is an example of versioning by convention; not every API uses this format.

### Path Parameters

Path parameters identify a particular resource.

Example:

`GET /students/101`

Here, `101` is the student ID.

### Query Parameters

Query parameters are commonly used for filtering, sorting, searching, and pagination.

Example:

`GET /students?department=CSE&limit=10`

Here:
- `department=CSE` filters by department.
- `limit=10` requests up to ten results.

Query parameters begin after `?`, and multiple parameters are separated using `&`.

### API Endpoint Examples

| Endpoint | Purpose |
|---|---|
| `GET /products` | Retrieve products |
| `GET /products/15` | Retrieve product 15 |
| `POST /products` | Create a product |
| `PATCH /products/15` | Update selected product fields |
| `DELETE /products/15` | Delete product 15 |

Good endpoint design usually uses clear, consistent resource names.

---

## 5. HTTP Request Structure

An HTTP request contains information that tells the server what the client wants to do.

A request commonly contains:

1. Request method
2. Request target or path
3. Headers
4. Optional request body

### Example Request

    POST /students HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    Accept: application/json

    {
      "name": "Ravi",
      "department": "CSE"
    }

Explanation:

- `POST` indicates that the client is submitting data to create a resource.
- `/students` identifies the resource collection.
- `Host` identifies the server.
- `Content-Type` indicates that the request body is JSON.
- `Accept` indicates that the client prefers a JSON response.
- The body contains the student information.

This is an illustrative HTTP request. Actual HTTP/2 and HTTP/3 communication uses different wire-level framing, even though the HTTP concepts remain applicable.

### What Is a Request Body?

The request body contains data sent to the server.

It is commonly used with POST, PUT, and PATCH requests.

Example JSON body:

    {
      "product": "Keyboard",
      "price": 1200
    }

A GET request generally does not need a request body; clients should use query parameters for typical filtering and retrieval operations.

---

## 6. HTTP Response Structure

An HTTP response contains the result of processing a request.

A response commonly includes:

1. Status code
2. Response headers
3. Optional response body

### Example Response

    HTTP/1.1 201 Created
    Content-Type: application/json

    {
      "id": 101,
      "name": "Ravi",
      "department": "CSE"
    }

Explanation:

- `201 Created` indicates that a resource was created successfully.
- `Content-Type` indicates that the response body is JSON.
- The response body contains the created student's details, including the assigned ID.

The exact response format and status code depend on the API's design.

---

## 7. HTTP Methods

HTTP methods specify the intended action for a request.

### GET

Used to retrieve a resource or collection of resources.

Example:

`GET /products`

It retrieves product information without intending to change server-side data.

GET is defined as a safe and idempotent method.

### POST

Used to submit data for processing. It is commonly used to create a resource.

Example:

`POST /products`

Request body:

    {
      "name": "Mouse",
      "price": 500
    }

POST is not inherently idempotent. Sending the same request multiple times may create multiple resources unless the API implements duplicate prevention or idempotency controls.

### PUT

Used to create or replace the state of a resource at a known target URI, depending on the API's design.

Example:

`PUT /products/15`

Request body:

    {
      "name": "Wireless Mouse",
      "price": 800
    }

PUT is idempotent by definition: repeating the same intended request should have the same intended effect as sending it once.

### PATCH

Used to apply a partial modification to a resource.

Example:

`PATCH /products/15`

Request body:

    {
      "price": 750
    }

The exact meaning of a PATCH document depends on the patch format and API implementation.

### DELETE

Used to request the removal of a resource.

Example:

`DELETE /products/15`

DELETE is idempotent by definition, although the response to repeated requests may differ. For example, the first request may return `204 No Content`, while a later request may return `404 Not Found`.

### HTTP Method Comparison

| Method | Common purpose | Request body | Idempotent? |
|---|---|---|---|
| GET | Retrieve data | Usually unnecessary | Yes |
| POST | Submit data or create resources | Commonly used | Not generally |
| PUT | Replace a resource | Commonly used | Yes |
| PATCH | Partially modify a resource | Commonly used | Not necessarily |
| DELETE | Remove a resource | Usually unnecessary | Yes |

Idempotency means that repeating the same request has the same intended effect on server state as performing it once.

---

## 8. HTTP Status Codes

Status codes communicate the outcome of an HTTP request.

They are divided into five categories.

### 1xx — Informational

The request has been received, and processing is continuing.

Example: `100 Continue`

### 2xx — Success

The request was successfully received, understood, and processed.

- `200 OK` — The request succeeded.
- `201 Created` — A resource was created.
- `202 Accepted` — The request was accepted for processing, but processing may not be complete.
- `204 No Content` — The request succeeded, and no response body is returned.

### 3xx — Redirection

The client needs to take additional action, commonly to follow a redirect.

- `301 Moved Permanently` — The resource has a permanent new location.
- `302 Found` — A temporary redirect.
- `304 Not Modified` — A cached representation may still be used.

### 4xx — Client Errors

The request cannot be fulfilled because of an issue associated with the request or the client's access.

- `400 Bad Request` — The request is invalid or malformed.
- `401 Unauthorized` — Valid authentication credentials are missing or were not accepted.
- `403 Forbidden` — The server refuses to authorize the request.
- `404 Not Found` — The requested resource was not found.
- `405 Method Not Allowed` — The method is not supported for that resource.
- `409 Conflict` — The request conflicts with the current state of a resource.
- `422 Unprocessable Content` — The request content cannot be processed according to the server's validation rules.
- `429 Too Many Requests` — The client has exceeded a rate limit.

### 5xx — Server Errors

The server failed to fulfill an otherwise valid request.

- `500 Internal Server Error` — An unexpected server-side error occurred.
- `502 Bad Gateway` — A gateway received an invalid response from an upstream server.
- `503 Service Unavailable` — The service is temporarily unable to handle the request.
- `504 Gateway Timeout` — A gateway did not receive a timely upstream response.

### Why Are Status Codes Important?

Status codes help applications decide what to do next.

For example:
- On `200`, process the returned data.
- On `401`, check authentication.
- On `404`, handle the missing resource.
- On `429`, respect the rate limit and any `Retry-After` guidance.
- On `500`, report the failure and retry only when appropriate.

---

## 9. HTTP Headers

HTTP headers carry additional metadata about requests and responses.

Headers can communicate content formats, authentication information, caching rules, and other request or response properties.

### Common Request Headers

**Content-Type**

Specifies the media type of the request body.

Example:

`Content-Type: application/json`

**Accept**

Indicates the response media types the client can accept.

Example:

`Accept: application/json`

**Authorization**

Carries authentication credentials or tokens according to the authentication scheme.

Example:

`Authorization: Bearer YOUR_ACCESS_TOKEN`

The placeholder must be replaced with a valid token when using a real service. Never publish real tokens in source code or documentation.

**User-Agent**

Identifies the client software making the request.

### Common Response Headers

**Content-Type:** Identifies the format of the response body.

**Cache-Control:** Specifies caching rules.

**Location:** Often identifies the location of a newly created resource or a redirect target.

**Retry-After:** May indicate how long a client should wait before retrying a request.

### Why Headers Matter

Headers help the client and server agree on data formats, apply authentication, manage caching, and communicate how a request should be handled.

---

## 10. JSON — JavaScript Object Notation

JSON is a lightweight data-interchange format commonly used by REST APIs.

Although its name refers to JavaScript, JSON is language-independent and is supported by Python, Java, JavaScript, and many other programming languages.

### Example JSON Object

    {
      "name": "Ravi",
      "age": 21,
      "department": "CSE",
      "skills": ["Python", "SQL", "REST APIs"],
      "is_intern": true
    }

### JSON Data Types

- String: `"Python"`
- Number: `21`
- Boolean: `true` or `false`
- Array: `["Python", "SQL"]`
- Object: `{"city": "Coimbatore"}`
- Null: `null`

JSON does not support comments, and its property names and string values must use double quotes.

### JSON vs Python Dictionaries

A Python dictionary can represent similar data:

    student = {
        "name": "Ravi",
        "age": 21,
        "is_intern": True
    }

Notice that Python uses `True`, whereas JSON uses `true`.

Python's `json` module converts between JSON and Python data structures.

    import json

    data = '{"name": "Ravi", "age": 21}'

    student = json.loads(data)

    print(student["name"])
    print(student["age"])

Output:

    Ravi
    21

The `json.loads()` function parses a JSON string into a Python object.

The `json.dumps()` function converts a Python object into a JSON string.

When using the `requests` library, `response.json()` is commonly used to parse a JSON response.

---

## 11. Authentication and Authorization

Authentication and authorization are related but different concepts.

### Authentication

Authentication verifies the identity of a user or application.

Examples include:
- API keys
- Username and password
- Access tokens
- OAuth 2.0-based authentication flows

### Authorization

Authorization determines what an authenticated user or application is allowed to do.

For example, an authenticated user may be allowed to view a student record but not delete it.

### API Keys

An API key is a credential that a service may use to identify or authenticate an application.

Example header:

    X-API-Key: YOUR_API_KEY

The exact header name depends on the API provider.

### Bearer Tokens

A bearer token is commonly sent in the Authorization header.

    Authorization: Bearer YOUR_ACCESS_TOKEN

Anyone who obtains a valid bearer token may be able to use its associated permissions. It must therefore be protected like a password.

### Important Security Practices

- Never commit real API keys, passwords, or access tokens to GitHub.
- Store secrets in environment variables or an appropriate secrets manager.
- Use HTTPS when transmitting credentials.
- Grant only the permissions required for the task.
- Rotate or revoke credentials if they are exposed.
- Do not print secrets in logs or error messages.

---

## 12. Rate Limiting and API Errors

### What Is Rate Limiting?

Rate limiting controls how frequently a client can make requests to an API.

A service may allow only a certain number of requests within a time window.

For example, an API might allow 100 requests per minute for a particular account.

Exceeding the limit may result in a `429 Too Many Requests` response.

The actual limits depend on the service and account.

### How to Handle Rate Limits

- Check the API provider's rate-limit documentation.
- Inspect response headers for remaining quotas or reset times when provided.
- Respect the `Retry-After` header when available.
- Use exponential backoff when retrying transient failures.
- Avoid repeatedly sending requests that will predictably fail.

### Common API Errors

| Problem | Possible cause | Suggested action |
|---|---|---|
| 400 Bad Request | Invalid request parameters | Check the URL, parameters, and body |
| 401 Unauthorized | Missing or invalid credentials | Verify authentication |
| 403 Forbidden | Insufficient permission | Check access permissions |
| 404 Not Found | Incorrect endpoint or missing resource | Verify the URL and resource ID |
| 429 Too Many Requests | Rate limit exceeded | Wait before retrying |
| 500 Internal Server Error | Server-side failure | Retry cautiously and check service status |
| Timeout | Server is slow or unreachable | Use timeouts and appropriate retry logic |

Not every failure should be retried. Authentication errors and malformed requests usually require correction rather than repetition.

---

## 13. API Versioning

API versioning helps providers introduce changes without unexpectedly breaking existing clients.

For example:

- `/api/v1/students`
- `/api/v2/students`

Versioning may also be implemented using headers or other conventions.

### Why Versioning Is Useful

- Allows APIs to evolve over time.
- Helps preserve compatibility with existing applications.
- Gives clients time to migrate to newer functionality.
- Makes breaking changes easier to manage.

The versioning strategy depends on the API provider.

---

## 14. Consuming an API Using Python

Python provides libraries that simplify HTTP communication.

The `requests` library is a common choice for making synchronous HTTP requests.

### Installation

    python -m pip install requests

### Example: Sending a GET Request

    import requests

    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        post = response.json()

        print("Title:", post["title"])
        print("Body:", post["body"])

    except requests.exceptions.Timeout:
        print("The request timed out.")

    except requests.exceptions.HTTPError as error:
        print("HTTP error:", error)

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)

### Explanation

- `requests.get()` sends an HTTP GET request.
- `timeout=10` limits how long the client waits for connection and response activity; it is not necessarily a strict ten-second total deadline.
- `raise_for_status()` raises an HTTP error for unsuccessful HTTP status codes.
- `response.json()` parses a JSON response.
- Exception handling allows the program to handle timeouts and HTTP or connection failures.

The example uses JSONPlaceholder, a public test API. Its sample data is intended for practice, not production use.

### Example: Sending Query Parameters

    import requests

    url = "https://jsonplaceholder.typicode.com/posts"

    params = {"userId": 1}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    posts = response.json()

    for post in posts:
        print(post["title"])

Passing parameters through `params` lets the library encode them correctly in the URL.

### Example: Sending JSON Data with POST

    import requests

    url = "https://jsonplaceholder.typicode.com/posts"

    data = {
        "title": "Learning REST APIs",
        "body": "Practicing Python requests",
        "userId": 1
    }

    response = requests.post(
        url,
        json=data,
        timeout=10
    )

    response.raise_for_status()

    print("Status:", response.status_code)
    print("Response:", response.json())

The `json` argument serializes the Python dictionary into JSON and sets an appropriate content type.

Public test APIs may simulate creation rather than permanently storing the submitted resource.

---

## 15. REST APIs in AI Application Development

APIs play an important role in building AI-powered applications.

### Example Architecture

    User Interface
          |
          v
    Python Backend
          |
          v
    REST API Request
          |
          v
    AI Model or External Service
          |
          v
    JSON Response
          |
          v
    Backend Processes Result
          |
          v
    User Interface Displays Output

### Common AI API Use Cases

**1. Generative AI**

A backend sends a prompt to a language model service and receives generated text.

**2. Machine learning inference**

An application sends input data to a model-serving endpoint and receives a prediction.

**3. Computer vision**

An application submits image data or an image reference to an appropriate service and receives labels or other analysis results.

**4. Retrieval-augmented generation (RAG)**

A backend can retrieve relevant documents and send context to a language model through an API.

**5. Data integration**

An AI application can retrieve information from external services, validate it, and use it as model input.

### Example

In a food-recognition application:

1. The user uploads a food image.
2. The backend validates the image.
3. A computer vision model identifies the food.
4. The backend requests recipe suggestions from a language model service.
5. The application returns the results to the user.

An API can connect these components while keeping their responsibilities separate.

---

## 16. Common API Design Best Practices

- Use meaningful, consistent resource names.
- Use HTTP methods according to their intended semantics.
- Return appropriate status codes.
- Validate incoming request data.
- Provide clear error messages without exposing sensitive internal details.
- Use pagination for large collections.
- Apply authentication and authorization where required.
- Set timeouts for outbound HTTP requests.
- Handle network errors and rate limits.
- Document endpoints, parameters, request bodies, and responses.
- Avoid exposing secrets in source code or logs.
- Use HTTPS in production.
- Version APIs when needed to manage compatibility.
- Test successful requests, invalid inputs, and failure cases.

---

## 17. Summary

HTTP provides the communication protocol used by clients and servers. REST provides architectural guidance for designing resource-oriented APIs. HTTP methods describe the intended action, status codes communicate the result, headers carry metadata, and JSON is a common format for exchanging structured data.

Python's `requests` library allows developers to consume existing APIs. These concepts are foundational for building backend services with FastAPI and integrating AI models into real-world applications.

### Key Takeaways

- API: A way for software systems to communicate.
- HTTP: A protocol for request-response communication.
- REST: An architectural style for designing networked APIs.
- Endpoint: A resource address accessed using an HTTP method.
- JSON: A common format for structured data exchange.
- Status code: Indicates the result of an HTTP request.
- Authentication: Verifies identity.
- Authorization: Determines permitted actions.
- Rate limiting: Restricts request frequency or volume.
- Python Requests: A library for consuming HTTP APIs.

### References

- MDN Web Docs — HTTP Overview: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview
- MDN Web Docs — HTTP Request Methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods
- MDN Web Docs — HTTP Response Status Codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
- REST Architectural Style — Roy Fielding's Dissertation: https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
- Requests Documentation: https://requests.readthedocs.io/en/latest/