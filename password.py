password = input("Enter password: ")
pswd = "Saksham"
count = 0
for i in range(3):
    if (password == pswd):
        print("successfully logged in")
        break
    else:
        print("failed to login")
