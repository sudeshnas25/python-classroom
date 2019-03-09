password = ''
for password in range(0,3):

    while password != 'python12345':
        password = input("Enter your password: ")
        if password == 'python12345':
            print("You are logged in")
        else:
            print("Sorry! Enter correct password")
print("you are blocked")
