import pandas as pd

# 1. Load the CSV dataset
df = pd.read_csv("day2/student_performance.csv")

# 2. Inspect the dataset
print("First five rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn information:")
df.info()

print("\nStatistical summary:")
print(df.describe())

# 3. Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# 4. Filter students scoring 90 or above
high_scorers = df[df["marks"] >= 90]
print("\nStudents scoring 90 or above:")
print(high_scorers)

# 5. Calculate average marks by subject
subject_average = df.groupby("subject")["marks"].mean()
print("\nAverage marks by subject:")
print(subject_average.round(2))

# 6. Sort students by marks
sorted_df = df.sort_values("marks", ascending=False)
print("\nStudents sorted by marks:")
print(sorted_df)

# 7. Export the processed dataset
sorted_df.to_csv("day2/sorted_student_performance.csv", index=False)

# 8. Save subject averages
subject_average.round(2).to_csv("day2/subject_averages.csv")

print("\nAnalysis completed successfully!")
