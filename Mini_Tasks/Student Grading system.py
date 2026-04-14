#========== Student Grading system ==========
def calculate_grade(percentage):
  if 90 <= percentage <= 100:
    return "A"
  elif 80 <= percentage < 90:
    return "B"
  elif 70 <= percentage < 80:
    return "C"
  elif 60 <= percentage < 70:
    return "D"
  else:
    return "Fail"

def main():
  print("============ Student Result System =========\n")

  # Student Information
  student_name = input("Enter your name: ")
  student_id = input("Enter your student id: ")
  student_class = input("Enter your class: ")

  #Subject marks
  subjects = ["English","Math","Urdu","Computer","Islamiat"]
  total_marks = 0

  for subject in subjects:
    while True:
      try:
        marks = int(input(f"Enter {subject} marks: "))
        if 0 <= marks <= 100:
          total_marks += marks
          break
        else:
          print("please enter number between 0 and 100:")
      except ValueError:
          print("please inter valid number")

  percentage = (total_marks/ 500)*100
  grade = calculate_grade(percentage)

      # Result Card
  print("\n========== RESULT CARD ==========")
  print(f"Name        : {student_name}")
  print(f"ID          : {student_id}")
  print(f"Class       : {student_class}")
  print(f"Total Marks : {total_marks}/500")
  print(f"Percentage  : {round(percentage, 2)}%")
  print(f"Grade       : {grade}")

  print("\nKeep working hard and keep improving!")

if __name__ == "__main__":
  main()
