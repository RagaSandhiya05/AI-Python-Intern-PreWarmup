# Student Marks Analyzer
import csv
import json

students = []

with open("day2/students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["marks"] = int(row["marks"])
        students.append(row)

total_marks = sum(student["marks"] for student in students)
average_marks = total_marks / len(students)

topper = max(students, key=lambda student: student["marks"])

summary = {
    "total_students": len(students),
    "average_marks": round(average_marks, 2),
    "topper": topper["name"],
    "highest_marks": topper["marks"]
}

with open("day2/summary.json", "w") as file:
    json.dump(summary, file, indent=4)

print("Student summary generated successfully!")
print(json.dumps(summary, indent=4))
