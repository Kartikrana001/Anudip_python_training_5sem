password = "admin123"

while True:
    user_pass = input("Enter Password: ")

    if user_pass == password:
        print("Login Successful.")
        break
    else:
        print("Invalid Password.")
