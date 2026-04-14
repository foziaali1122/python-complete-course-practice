#Task: Email validator
email = input("Enter your email: ")

#check Space
if " " in email:
  print("Invalid email: space is not allowed.")
#check @
elif email.count("@") != 1:
  print("Invalid email: Must be 1 @ contain in email.")
#Split username or domain
else:
  username , domain = email.split("@")

  #check username length
  if len(username) < 3:
    print("Invalid email: email must be 3 charachters.")
  #check "." in domain
  elif "." not in domain:
    print("Invalid email: email must contain .")
  #check domain
  elif not(domain.endswith("com") or domain.endswith("pk")):
    print("Invalid email: ")

  #final valid email
  print('valid email')
  print("Username\t:", username)
  print("Username length:", len(username))
  print("Domain\t: ", domain)
