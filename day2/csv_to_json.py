# Student Marks Analyzer
import json
import csv

from student_utils import (
    load_students,
    generate_summary,
    InvalidStudentDataError
)


def main():
    input_file = "day2/students.csv"
    output_file = "day2/summary.json"

    try:
        students = load_students(input_file)
        summary = generate_summary(students)

        with open(
            output_file, "w", encoding="utf-8"
        ) as file:
            json.dump(summary, file, indent=4)

    except FileNotFoundError:
        print(f"Error: Input file not found: {input_file}")

    except PermissionError:
        print("Error: Permission denied while accessing a file.")

    except InvalidStudentDataError as error:
        print(f"Invalid student data: {error}")

    except csv.Error as error:
        print(f"CSV processing error: {error}")

    except OSError as error:
        print(f"File operation failed: {error}")

    else:
        print("Student summary generated successfully!")
        print(json.dumps(summary, indent=4))

    finally:
        print("CSV processing attempt completed.")


if __name__ == "__main__":
    main()
