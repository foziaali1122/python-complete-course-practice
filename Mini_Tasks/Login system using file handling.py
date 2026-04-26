# Registration
with open("users.txt", "a") as file:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    file.write(f"{username},{password}\n")

# Login
username = input("Enter login username: ").strip()
password = input("Enter login password: ").strip()

found = False
with open("users.txt", "r") as file:
    for line in file:
        u, p = line.strip().split(",")
        if u == username and p == password:
          found = True
          break

if found:
    print("Login successful!")
else:
    print("Invalid username or password.")
