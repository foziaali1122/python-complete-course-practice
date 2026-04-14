#Task : Student Result System
def student_result_system(percentage):
    if percentage >= 70:
        return "A grade"
    elif percentage >= 60:
        return "B grade"
    elif percentage >= 50:
        return "C grade"
    elif percentage >= 40:
        return "D grade"
    else:
        return "Fail"

students = int(input("Enter number of students: "))

for student in range(1, students + 1):
    print(f"\n--- Student {student} ---")

    name = input("Enter name: ")
    Class = input("Enter class: ")

    marks1 = int(input("English marks: "))
    marks2 = int(input("Math marks: "))
    marks3 = int(input("Science marks: "))

    obtained_marks = marks1 + marks2 + marks3
    percentage = (obtained_marks * 100) / 300

    grade = student_result_system(percentage)

    print("\n======= Result ======")
    print("Name\t:", name)
    print("Class\t:", Class)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade\t:", grade)
