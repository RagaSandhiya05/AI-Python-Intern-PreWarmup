import csv

class InvalidStudentDataError(Exception):
    """Raised when student data is invalid."""
    pass

def load_students(file_path):
    students = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        required_columns = {"name", "subject", "marks"}

        if not reader.fieldnames or not required_columns.issubset(
            reader.fieldnames
        ):
            raise InvalidStudentDataError(
                "CSV must contain name, subject, and marks columns."
            )

        for line_number, row in enumerate(reader, start=2):
            name = (row.get("name") or "").strip()
            subject = (row.get("subject") or "").strip()
            marks_text = (row.get("marks") or "").strip()

            if not name or not subject or not marks_text:
                raise InvalidStudentDataError(
                    f"Missing data on line {line_number}."
                )

            try:
                marks = int(marks_text)
            except ValueError:
                raise InvalidStudentDataError(
                    f"Marks must be an integer on line {line_number}."
                )

            if not 0 <= marks <= 100:
                raise InvalidStudentDataError(
                    f"Marks must be between 0 and 100 "
                    f"on line {line_number}."
                )

            students.append({
                "name": name,
                "subject": subject,
                "marks": marks
            })

    if not students:
        raise InvalidStudentDataError(
            "The CSV file contains no student records."
        )

    return students

def generate_summary(students):
    total_marks = sum(student["marks"] for student in students)
    average_marks = total_marks / len(students)
    topper = max(students, key=lambda student: student["marks"])

    return {
        "total_students": len(students),
        "average_marks": round(average_marks, 2),
        "topper": topper["name"],
        "highest_marks": topper["marks"]
    }
