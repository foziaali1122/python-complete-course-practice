#task: ATM System

balance = 1000

while True:
  print("\n===== Menue =====")
  print("1. Withdraw")
  print("2. Deposit")
  print("3. Check balance")
  print("4. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    amount = int(input("Enter amount for withdraw: "))
    if amount <= balance:
      balance -= amount
      print("Withdraw successful")
    else:
      print("Insufficient balance")

  elif choice == "2":
    amount = int(input("Enter amount for deposit: "))
    balance += amount
    print("Your deposit is added")

  elif choice == "3":
    print("Your balance is: ", balance)
    
  elif choice == "4":
    print("Thank you! Exiting...")
    break
  else:
    print("Invalid choice")
