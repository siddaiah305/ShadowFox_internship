import csv


file_path = r"C:\Users\kasan\OneDrive\Documents\student_marks.csv"
output_path = r"C:\Users\kasan\OneDrive\Documents\student_marks_final.csv"

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    students = [dict(row) for row in reader]


for student in students:
    marks = [int(student[subject]) for subject in student if subject not in ["Name", "Roll No"]]
    student["Total_Marks"] = sum(marks)
    student["Average"] = round(sum(marks) / len(marks), 2)  # Round average to 2 decimal places

with open(output_path, "w", newline="", encoding="utf-8") as file:
    fieldnames = students[0].keys()  # Get all column names
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("Updated file saved successfully at:", output_path)
