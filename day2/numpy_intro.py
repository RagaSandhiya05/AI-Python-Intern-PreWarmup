import numpy as np

marks = np.array([85, 92, 78, 96, 88])

print("Marks:", marks)
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Standard deviation:", round(np.std(marks), 2))

passed = marks[marks >= 80]
print("Marks >= 80:", passed)
