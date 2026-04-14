#Task: Number Guessing Game
secrect_num = 8

for i in range(1, 4):
  guess = int(input("Enter the number: "))
  
  if guess == secrect_num:
    print("Congratulations! You guess the right number")
  elif guess > secrect_num:
    print("Number is too high. Please try again")
  elif guess < secrect_num:
    print("Number is too low. Please try again")
  else:
    print("Game over! The number was 8")
