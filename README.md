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
