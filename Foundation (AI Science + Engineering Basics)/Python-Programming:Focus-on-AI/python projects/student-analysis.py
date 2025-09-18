# Week 1: Basics
def add_student(students):
    name = input("Enter student name: ")
    grades = []
    for i in range(3):  # collect 3 grades
        grade = float(input(f"Enter grade for subject {i+1}: "))
        grades.append(grade)
    students[name] = grades
    print(f"{name}'s grades saved!")

def show_report(students):
    if not students:
        print("No student data available yet.")
        return
    for name, grades in students.items():
        avg = sum(grades) / len(grades)
        print(f"{name} → Grades: {grades}, Average: {avg:.2f}")

students = {}
while True:
    print("\n1. Add Student  2. Show Report  3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student(students)
    elif choice == "2":
        show_report(students)
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
