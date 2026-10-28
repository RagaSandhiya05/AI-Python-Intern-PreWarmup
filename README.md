# 💻 AI Python Intern Pre-Warmup

A collection of hands-on tasks and Python practice programs completed as part of my AI Python Intern Pre-Warmup journey. This repository tracks my progress in Python fundamentals, development environment setup, version control, and problem-solving.

---

## 📅 Day 1 – Environment Setup & Python Fundamentals

Day 1 focuses on setting up the Python development environment, configuring Git for version control, and strengthening Python programming skills through practical exercises.

### 📌 Tasks Completed

| Task | Topic | File / Resource | Description |
|---|---|---|---|
| T01 | Environment Setup | `.venv/`, `.gitignore` | Set up the Python development environment using a virtual environment and configured Git to ignore unnecessary files |
| T02 | Git & Version Control | Git repository | Initialized the Git repository, configured Git identity, and practiced staging, committing, and pushing changes |
| T03 | Python Basics | [`basics.py`](day1/basics.py) | Practiced variables, data types, operators, conditional statements, loops, and basic programming problems |
| T04 | Functions | [`exercises.py`](day1/exercises.py) | Solved common programming problems using reusable Python functions |
| T05 | Data Structures | [`word_count.py`](day1/word_count.py) | Built a word-frequency counter that identifies and displays the top five most frequent words in a paragraph |

### 🛠️ Concepts & Skills Practiced

- **Environment Setup:** Python virtual environments and dependency isolation
- **Version Control:** Git initialization, configuration, staging, commits, and remote repository management
- **Python Fundamentals:** Variables, data types, operators, conditionals, and loops
- **Problem-Solving:** Factorials, prime numbers, Fibonacci series, and palindrome checking
- **Functions:** Defining and calling reusable functions
- **Data Structures:** Lists, tuples, dictionaries, and sets
- **Python Techniques:** String manipulation, sorting, slicing, and comprehensions

### 📂 Day 1 Learning Structure

```text
AI-Python-Intern-PreWarmup/
└── day1/
    ├── basics.py
    ├── exercises.py
    ├── word_count.py
    └── T01_python_version_venv_active.png
```

### ▶️ How to Run

Run the Python programs from the repository's root directory:

```bash
python day1/basics.py
python day1/exercises.py
python day1/word_count.py
```

### 📚 Learning Resources

- [Python Tutorial – Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Official Documentation](https://docs.python.org/3/)
- [Pro Git Book](https://git-scm.com/book/en/v2)

### ✅ Day 1 Outcome

- Set up a Python development environment.
- Established a Git-based version control workflow.
- Practiced Python fundamentals and function-based programming.
- Applied built-in data structures to a practical word-frequency analysis problem.

---

## 📅 Day 2 – File Handling, OOP & Data Analysis

Day 2 focuses on handling structured data using CSV and JSON files, writing reusable Python modules, implementing object-oriented programming concepts, performing data analysis using NumPy and pandas, and practicing Git branching and merging workflows.

### 📌 Tasks Completed

| **Task** | **Topic** | **File / Resource** | **Description** |
| -------- | --------- | ------------------- | --------------- |
| T06 | File Handling & JSON | [`csv_to_json.py`](day2/csv_to_json.py), [`students.csv`](day2/students.csv), `summary.json` | Read student marks from a CSV file, process the data, and generate a JSON summary. |
| T07 | Exception Handling & Modules | [`student_utils.py`](day2/student_utils.py), [`csv_to_json.py`](day2/csv_to_json.py) | Implemented exception handling and reusable functions using a separate Python module. |
| T08 | Object-Oriented Programming | [`oop_demo.py`](day2/oop_demo.py) | Practiced classes, objects, constructors, instance attributes, and methods through a bank account demonstration. |
| T09 | NumPy & pandas | [`numpy_intro.py`](day2/numpy_intro.py), [`pandas_intro.py`](day2/pandas_intro.py), [`student_performance.csv`](day2/student_performance.csv) | Used NumPy for array operations and pandas for reading, sorting, analyzing, and exporting student performance data. |
| T10 | Git Branching & Merging | Git branches and practice files | Practiced branch creation, merging, merge conflict resolution, stashing, restoring changes, and reverting commits. |

### 🛠️ Concepts & Skills Practiced

- **File Handling:** Reading CSV files and writing structured JSON output
- **Data Processing:** Extracting student information, calculating summaries, and organizing results
- **Exception Handling:** Handling invalid input, missing files, and runtime errors
- **Python Modules:** Importing and reusing functions across Python files
- **Object-Oriented Programming:** Classes, objects, constructors, attributes, methods, and encapsulation basics
- **NumPy:** Array creation, numerical operations, and basic statistical calculations
- **pandas:** DataFrame operations, CSV loading, sorting, subject averages, and exporting results
- **Version Control:** Git branching, merging, conflict resolution, stash, restore, and revert
- **Dependency Management:** Installing and recording project dependencies in `requirements.txt`

### 📂 Day 2 Learning Structure

```text
day2/
├── T10_Git_History.png
├── csv_to_json.py
├── git-practice.txt
├── numpy_intro.py
├── oop_demo.py
├── pandas_intro.py
├── sorted_student_performance.csv
├── student_performance.csv
├── student_utils.py
├── students.csv
├── subject_averages.csv
└── summary.json
```


### ▶️ How to Run

Run the following commands from the repository's root directory after activating your virtual environment.

**1. Install the required dependencies**

```bash
pip install -r requirements.txt
```

**2. Run the CSV-to-JSON analyzer**

```bash
python day2/csv_to_json.py
```

**3. Run the OOP demonstration**

```bash
python day2/oop_demo.py
```

**4. Run the NumPy program**

```bash
python day2/numpy_intro.py
```

**5. Run the pandas program**

```bash
python day2/pandas_intro.py
```

### 📚 Learning Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python – Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python – Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python – Classes](https://docs.python.org/3/tutorial/classes.html)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [Pro Git Book – Branching](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

### ✅ Day 2 Outcome

- Processed structured data using CSV and JSON files.
- Implemented reusable modules and exception handling.
- Applied object-oriented programming concepts through a bank account example.
- Performed numerical operations and tabular data analysis using NumPy and pandas.
- Generated processed datasets and summary output files.
- Practiced Git workflows for managing branches, resolving conflicts, and handling changes.

---

## 📅 Day 3 – API Integration, Testing & Development

Day 3 focuses on consuming external APIs using Python, testing HTTP requests with Postman and cURL, building REST APIs using FastAPI, and managing secrets securely through environment variables.

### 📌 Tasks Completed

| **Task** | **Topic** | **File / Resource** | **Description** |
| -------- | --------- | ------------------- | --------------- |
| T11 | API Fundamentals | `api_notes.md` | Studied API concepts, REST architecture, HTTP methods, status codes, request headers, JSON responses, and API communication. |
| T12 | API Consumption | [`weather_api.py`](https://github.com/RagaSandhiya05/AI-Python-Intern-PreWarmup/blob/main/day3/weather_api.py), `requirements.txt` | Consumed the Open-Meteo weather API using Python's `requests` library, processed JSON responses, and implemented request error handling. |
| T13 | API Testing | `api_testing.md`, `screenshots/` | Tested GET and POST requests using Postman and cURL, inspected response bodies and headers, and tested an HTTP 404 error response. |
| T14 | FastAPI Development | [`app/main.py`](https://github.com/RagaSandhiya05/AI-Python-Intern-PreWarmup/blob/main/day3/app/main.py) | Built a REST API using FastAPI with health-check, item retrieval, and item creation endpoints, including request validation using Pydantic. |
| T15 | Secrets & Environment Variables | `.env`, `.env.example`, `.gitignore`, `test_env.py` | Practiced loading environment variables using `python-dotenv`, protecting sensitive values with `.gitignore`, and creating an example environment configuration file. |

### 🛠️ Concepts & Skills Practiced

- **API Fundamentals:** REST APIs, client-server communication, endpoints, HTTP methods, request parameters, headers, and JSON
- **API Consumption:** Sending GET requests using Python's `requests` library and processing API responses
- **Error Handling:** Request timeouts, connection errors, unsuccessful HTTP responses, and response validation
- **API Testing:** Testing GET and POST requests using Postman and cURL
- **HTTP Status Codes:** Understanding successful responses, resource-not-found errors, and request validation errors
- **FastAPI:** Creating REST API endpoints, defining route parameters, returning JSON responses, and running a development server with Uvicorn
- **Pydantic:** Validating request data, enforcing field constraints, and handling invalid input
- **Swagger UI:** Exploring interactive API documentation and testing endpoints through `/docs`
- **Environment Variables:** Loading configuration values using `python-dotenv` and `os.environ` / `os.getenv()`
- **Secret Management:** Using `.env`, `.env.example`, and `.gitignore` to prevent accidental exposure of sensitive values
- **Dependency Management:** Recording project dependencies in `requirements.txt`

### 📂 Day 3 Learning Structure

```text
day3/
├── app/
│   └── main.py
├── screenshots/
│   ├── 01_get_weather.png
│   ├── 02_post_request.png
│   ├── 03_error_response.png
│   ├── 04_fastapi_swagger.png
│   ├── 05_health_check.png
│   ├── 06_get_item.png
│   ├── 07_create_item.png
│   └── 08_validation_error.png
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── api_notes.md
├── api_testing.md
├── docker-compose.yml
├── requirements.txt
├── test_env.py
└── weather_api.py
```

*Note: The `.env` file stores local environment variables and is excluded from version control to protect sensitive information. The `.env.example` file provides a template without exposing actual secrets.*

### ▶️ How to Run

Run the following commands from the repository's root directory after activating your virtual environment.

**1. Install the required dependencies**

```bash
python -m pip install -r day3/requirements.txt
```

**2. Run the weather API client**

```bash
python day3/weather_api.py
```

**3. Run the FastAPI application**

```bash
cd day3
python -m uvicorn app.main:app --reload
```

**4. Open the interactive API documentation**

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) after starting the FastAPI server to explore and test the available endpoints.

**5. Test environment variable loading**

Open a separate terminal from the repository root and run:

```bash
python day3/test_env.py
```

Ensure that `day3/.env` exists locally and contains the required configuration values before running the environment variable test.

### 📚 Learning Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [Open-Meteo API Documentation](https://open-meteo.com/en/docs)
- [Postman Learning Center](https://learning.postman.com/)
- [cURL Documentation](https://curl.se/docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)
- [python-dotenv on PyPI](https://pypi.org/project/python-dotenv/)
- [Python `os` Module](https://docs.python.org/3/library/os.html)
- [Git Documentation](https://git-scm.com/doc)

### ✅ Day 3 Outcome

- Consumed an external weather API using Python and processed JSON responses.
- Tested HTTP requests and inspected API responses using Postman and cURL.
- Developed a REST API with FastAPI and implemented health-check, retrieval, and creation endpoints.
- Applied Pydantic validation to incoming request data and tested error responses.
- Explored interactive API documentation using Swagger UI.
- Managed application configuration using environment variables and `python-dotenv`.
- Practiced secure secret management using `.env.example` and `.gitignore`.
- Documented API development workflows and organized practical evidence through screenshots.

---

## 📅 Day 4 – Docker, Containerization & Git Collaboration

Day 4 focuses on understanding Docker fundamentals, practicing essential Docker CLI commands, containerizing the FastAPI application developed on Day 3, running multiple services using Docker Compose, and practicing Git collaboration workflows through branches, pull requests, code reviews, and GitHub Issues.

### 📌 Tasks Completed

| **Task** | **Topic** | **File / Resource** | **Description** |
| -------- | --------- | ------------------- | --------------- |
| T16 | Docker Fundamentals | Docker Desktop, `docker --version`, `docker info` | Installed and verified Docker Desktop, checked Docker Engine availability, and explored basic containerization concepts. |
| T17 | Docker CLI Commands | [`docker_cheatsheet.md`](day4/docker_cheatsheet.md), `screenshots/` | Practiced essential Docker commands for working with images and containers, including running containers, listing active containers, and mapping ports. |
| T18 | FastAPI Containerization | [`Dockerfile`](day3/Dockerfile), [`.dockerignore`](day3/.dockerignore) | Created a Docker image for the FastAPI application, configured the required dependencies, and ran the container with port mapping to access the API. |
| T19 | Docker Compose | [`docker-compose.yml`](day3/docker-compose.yml) | Used Docker Compose to build and run the FastAPI service alongside a Redis container, practicing multi-container application setup. |
| T20 | Git Collaboration | [`collaboration-practice.md`](day4/collaboration-practice.md), [Pull Request #1](https://github.com/RagaSandhiya05/AI-Python-Intern-PreWarmup/pull/1), [Issue #2](https://github.com/RagaSandhiya05/AI-Python-Intern-PreWarmup/issues/2) | Practiced creating a feature branch, committing and pushing changes, opening a pull request, submitting a review comment, merging into `main`, and creating a GitHub Issue. |

### 🛠️ Concepts & Skills Practiced

- **Docker Fundamentals:** Images, containers, registries, port mapping, and container lifecycle.
- **Docker CLI:** Running containers, listing containers, inspecting images, and managing container execution.
- **Dockerfile:** Defining a Python base image, setting a working directory, installing dependencies, copying application files, and configuring the startup command.
- **`.dockerignore`:** Excluding unnecessary files and local configuration from the Docker build context.
- **FastAPI Containerization:** Building a Docker image and exposing the API through a mapped port.
- **Docker Compose:** Defining and running multiple services, including FastAPI and Redis.
- **Git Branching:** Creating and working with feature branches.
- **Pull Requests:** Proposing changes, reviewing code or documentation, and merging changes into the main branch.
- **Code Review:** Adding review comments and understanding the feedback workflow.
- **GitHub Issues:** Creating issues to track documentation and follow-up work.

### 📂 Day 4 Learning Structure

```text
AI-Python-Intern-PreWarmup/
└── day4/
    ├── collaboration-practice.md
    ├── docker_cheatsheet.md
    └── screenshots/
        ├── docker-ps-running-container.png
        ├── fastapi-docker-container.png
        ├── fastapi-docker-docs.png
        ├── fastapi-docker-health.png
        ├── github-issue.png
        ├── merged-pull-request.png
        └── nginx-welcome.png
```

*Note: The screenshots folder contains evidence of Docker container execution, FastAPI testing, the Nginx welcome page, and GitHub collaboration activities. The Dockerfile, `.dockerignore`, and Docker Compose configuration are maintained separately for the FastAPI containerization tasks.*

### ▶️ How to Run

Run Docker commands from the repository root unless otherwise specified. Ensure Docker Desktop is running before executing the commands.

**1. Verify Docker installation**

```powershell
docker --version
docker compose version
docker info
```

**2. Run a test container**

```powershell
docker run hello-world
```

**3. Run the Nginx container**

```powershell
docker run -d --name day4-nginx -p 8080:80 nginx
docker ps
```

Open [http://localhost:8080](http://localhost:8080) in your browser to view the Nginx welcome page.

**4. Build the FastAPI Docker image**

```powershell
docker build -t intern-warmup-api ./day3
```

**5. Run the FastAPI container**

```powershell
docker run -d --name intern-warmup-api -p 8000:8000 intern-warmup-api
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) to explore the FastAPI Swagger UI.

**6. Start FastAPI and Redis using Docker Compose**

```powershell
docker compose -f day3/docker-compose.yml up --build -d
```

Check the running services:

```powershell
docker compose -f day3/docker-compose.yml ps
```

Stop the Compose services when finished:

```powershell
docker compose -f day3/docker-compose.yml down
```

*Note: If you already have containers using the same names or ports, stop or remove the conflicting containers before running the commands. Avoid running the standalone FastAPI container and the Compose version simultaneously if both use host port 8000.*

### 📚 Learning Resources

- [Docker Get Started](https://docs.docker.com/get-started/)
- [Docker CLI Reference](https://docs.docker.com/reference/cli/docker/)
- [Dockerfile Reference](https://docs.docker.com/reference/dockerfile/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Redis Documentation](https://redis.io/docs/)
- [GitHub Pull Requests Documentation](https://docs.github.com/en/pull-requests)
- [GitHub Issues Documentation](https://docs.github.com/en/issues)

### ✅ Day 4 Outcome

- Understood Docker fundamentals and verified the Docker environment.
- Practiced running and inspecting containers using Docker CLI commands.
- Containerized the FastAPI application using a Dockerfile and `.dockerignore`.
- Ran FastAPI and Redis services together using Docker Compose.
- Practiced Git branching, pushing changes, creating and reviewing pull requests, and merging changes into `main`.
- Created a GitHub Issue and organized screenshots as evidence of the completed learning tasks.

---

## 📅 Day 5 – Documentation, HTTPX & Containerized API

Day 5 focuses on exploring official technical documentation, learning a new Python library, building a weather summary REST API using FastAPI and HTTPX, containerizing the application using Docker, and completing GitHub documentation and Pull Request workflows.

### 📌 Tasks Completed

| Task | Topic | File / Resource | Description |
|---|---|---|---|
| T21 | Documentation Scavenger Hunt | [`docs_hunt.md`](docs_hunt.md) | Explored official documentation for Python, Requests, FastAPI, Docker, and Git to understand important features and commands. |
| T22 | Learn a New Python Library | [`new_library_demo.py`](new_library_demo.py), [`new_library_reflection.md`](new_library_reflection.md) | Learned HTTPX, made an HTTP GET request to a sample API, processed the JSON response, and handled HTTP errors. |
| T23 | Mini-Project: Containerized API | [`capstone/`](capstone/) | Built a Weather Summary API using FastAPI and HTTPX, integrated Open-Meteo APIs, processed weather data, handled errors, and containerized the application using Docker. |
| T24 | README, GitHub Pull Request & Demo | [`capstone/README.md`](capstone/README.md), [GitHub Pull Request](https://github.com/RagaSandhiya05/AI-Python-Intern-PreWarmup/pulls), [`capstone/screenshots/`](capstone/screenshots/) | Documented the API setup and usage, created a feature branch, submitted and merged a Pull Request, and prepared a five-minute mentor demonstration. |

### 🛠️ Concepts & Skills Practiced

**Technical Documentation:** Navigating official documentation, locating relevant information, and recording findings.

**HTTPX:** Sending HTTP requests, setting request timeouts, processing JSON responses, and handling HTTP errors.

**FastAPI:** Creating REST API endpoints, accepting query parameters, returning structured JSON responses, and documenting endpoints through Swagger UI.

**External API Integration:** Using the Open-Meteo Geocoding API to obtain city coordinates and the Weather Forecast API to retrieve weather information.

**Data Processing:** Extracting current weather details and calculating the average temperature from the next six hourly forecast values.

**Error Handling:** Handling unknown cities, external API failures, and unexpected response data with appropriate HTTP status codes.

**Environment Configuration:** Using environment variables and `python-dotenv` to configure API endpoints and request timeouts.

**Docker Containerization:** Building Docker images, running containers, mapping ports, loading environment variables, and inspecting container logs.

**Git & GitHub:** Creating feature branches, committing and pushing changes, opening Pull Requests, and merging changes into `main`.

**Technical Documentation:** Writing a detailed README with setup instructions, sample requests and responses, a system architecture diagram, Docker commands, and testing evidence.

### 📂 Day 5 Learning Structure

```text
day5/
├── docs_hunt.md
├── new_library_demo.py
├── new_library_reflection.md
└── capstone/
    ├── main.py
    ├── requirements.txt
    ├── Dockerfile
    ├── .dockerignore
    ├── README.md
    └── screenshots/
        ├── 01_home_endpoint.png
        ├── 02_weather_api_response.png
        ├── 03_swagger_ui.png
        ├── 04_unknown_city_error.png
        ├── 05_docker_image_build.png
        ├── 06_docker_container_running.png
        ├── 07_containerized_api_response.png
        └── T24_01_merged_pull_request.png
```

*Note: The `.env` file is used for local configuration and is not included in the repository. The `.dockerignore` file prevents it from being copied into the Docker image.*

### ▶️ How to Run

Run the following commands from the repository root after activating your virtual environment.

**1. Install the Day 5 dependencies**

```powershell
python -m pip install httpx fastapi "uvicorn[standard]" python-dotenv
```

**2. Run the HTTPX demonstration**

```powershell
python day5/new_library_demo.py
```

**3. Start the Weather Summary API locally**

```powershell
python -m uvicorn main:app --app-dir day5/capstone --reload
```

**4. Test the API**

Open the following URLs in your browser:

- Home endpoint: `http://127.0.0.1:8000/`
- Weather summary: `http://127.0.0.1:8000/weather?city=Coimbatore`
- Swagger UI: `http://127.0.0.1:8000/docs`

**5. Build the Docker image**

```powershell
docker build -t weather-summary-api:1.0 ./day5/capstone
```

**6. Run the Docker container**

Ensure the `.env` file exists inside `day5/capstone/` and port `8000` is available.

```powershell
docker run -d --env-file day5/capstone/.env -p 8000:8000 --name weather-api weather-summary-api:1.0
```

Verify the container:

```powershell
docker ps
```

View its logs:

```powershell
docker logs weather-api
```

**7. Stop the Docker container**

```powershell
docker stop weather-api
```

Remove it when no longer needed:

```powershell
docker rm weather-api
```

### 📚 Learning Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [HTTPX Documentation](https://www.python-httpx.org/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Open-Meteo API Documentation](https://open-meteo.com/en/docs)
- [Docker Documentation](https://docs.docker.com/)
- [Dockerfile Reference](https://docs.docker.com/reference/dockerfile/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Pull Requests Documentation](https://docs.github.com/en/pull-requests)

### ✅ Day 5 Outcome

- Explored official technical documentation and recorded key findings.
- Learned HTTPX and practised making HTTP requests and processing JSON responses.
- Developed a Weather Summary API using FastAPI and integrated external weather services.
- Implemented query parameter validation and error handling.
- Configured application settings using environment variables.
- Built and tested a Docker image and container for the API.
- Documented the application with setup instructions, sample responses, and an architecture diagram.
- Practised GitHub feature branch and Pull Request workflows.
- Prepared a five-minute demonstration covering the API, Docker deployment, and documentation.

### 🎯 Overall Learning Outcome

Completed five days of hands-on preparation covering Python fundamentals, file handling, object-oriented programming, data analysis, API development, testing, Docker containerization, Git collaboration, and technical documentation as preparation for an AI Python internship.

---
