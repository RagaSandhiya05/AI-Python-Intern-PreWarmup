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

### 📂 Day 1 Project Structure

```text
AI-Python-Intern-PreWarmup/
└── day1/
    ├── basics.py
    ├── exercises.py
    ├── word_count.py
    └── T01_python_version_venv_active
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

### 📂 Day 2 Project Structure

```text
AI-Python-Intern-PreWarmup/
├── day2/
│   ├── students.csv
│   ├── csv_to_json.py
│   ├── student_utils.py
│   ├── summary.json
│   ├── oop_demo.py
│   ├── student_performance.csv
│   ├── numpy_intro.py
│   ├── pandas_intro.py
│   ├── sorted_student_performance.csv
│   └── subject_averages.csv
└── requirements.txt
```

*Note: Git practice files and temporary demonstration files are not included in this structure.*

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

### 📂 Day 3 Project Structure

```text
AI-Python-Intern-PreWarmup/
└── day3/
    ├── api_notes.md
    ├── weather_api.py
    ├── api_testing.md
    ├── requirements.txt
    ├── app/
    │   └── main.py
    ├── test_env.py
    ├── .env.example
    ├── .gitignore
    └── screenshots/
        ├── 01_get_weather.png
        ├── 02_post_request.png
        ├── 03_error_response.png
        ├── 04_fastapi_swagger.png
        ├── 05_health_check.png
        ├── 06_get_item.png
        ├── 07_create_item.png
        └── 08_validation_error.png
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
