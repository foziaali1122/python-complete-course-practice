#Task : Mini Calculator (Advanced)

try:
  def add(num1 , num2):
      return num1 + num2
  def subtract(num1 , num2):
        return num1 - num2
  def multiplay(num1 , num2):
        return num1 * num2
  def devide(num1 , num2):
        if num2 == 0:
          return "Error: Cannot divided by zero"
        return num1 / num2
  def exponnent(num1 , num2):
      if num2 > 10:
        return "Power too large"
      return num1 ** num2
#main
  while True:
      print("\n===== Menue =====")
      print("1. Add")
      print("2. Subtract")
      print("3. Multiplay")
      print("4. Divide")
      print("5. Exponnent")
      print("6. Exit")

      choice = input("Enter your choice (1-5): ")

      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))


      if choice == "1":
            print(add(num1, num2))
      elif choice == "2":
            print(subtract(num1, num2))
      elif choice == "3":
            print(multiplay(num1, num2))
      elif choice == "4":
            print(devide(num1, num2))
      elif choice == "5":
            print(exponnent(num1, num2))
      elif choice == "6":
            print("Exiting.....")
            break

except Exception as e:
  print("Error", e)
