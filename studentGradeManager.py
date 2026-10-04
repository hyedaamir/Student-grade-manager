# Student Grade Manager
# Day 9-12 Dictionaries and Nested Dictionaries
students = {
    "Hyeda": {
        "Math": 85,
        "English": 78,
        "Computer": 92
    },
    "Zara": {
        "Math": 90,
        "English": 88,
        "Computer": 95
    },
    "Abdullah": {
        "Math": 70,
        "English": 75,
        "Computer": 80
    }
}
print("Student Grades")
for student, subjects in students.items():
    print("\nStudent:", student)
    for subject, grade in subjects.items():
        print(subject, ":", grade)
print("\nStudent Results")

for student, subjects in students.items():
    total = sum(subjects.values())
    average = total / len(subjects)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print(student)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print()