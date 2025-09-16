# Documented-By-Lamar
from name_art import print_name

# Print ASCII art name
print_name()

# Typecasting example inputs
name = input("Please enter your name: ").strip()
age = int(input("Please enter your current age: "))
gpa = float(input("Please enter your GPA: "))
student_input = input("Are you a student?: ").strip().lower()

if student_input in ("yes", "y", "yeah", "yeap"):
    print(f"Hello there {name}, you are {age} years old with a GPA of {gpa}.")
elif student_input in ("no", "n", "nah"):
    print(f"You are too smart for me to believe that you are not a student, {name}.")
else:
    print(f"That was an invalid choice, {name}.")
