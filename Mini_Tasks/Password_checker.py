#Task 38: Password Checker
password = input("Enter the password: ")
digit_count = 0
alpha_count = 0

#Loop for iterate over input
for char in password:
    if char.isdigit():   #check if digit is in password then count
      digit_count += 1
    elif char.isalpha(): #check if alphabates is in password then count
      alpha_count += 1

#display password and count
print("\nPassword\t:",password)
print("Digit counts\t:",digit_count)
print("Alphabates count:",alpha_count,"\n")

#Check Length
if len(password) >= 8:
  print("Password length is correct.")
else:
  print("Password length must be 8 characters")

#Check Digit counts
if digit_count >= 3:
  print("Your enter correct length of digits")
else:
    print("Digit must be 3 numbers")

#check Alpha counts
if alpha_count >= 5:
  print("Your enter correct length of alphabates")
else:
    print("Password have must be 5 alphabates")
