# The following program uses a while loop to check if the input password is correct.
guessed = False

while not guessed:
    password = input("Enter a password: ")
    if password == "prohack":
        guessed = True
        print("Access Granted!")
    else:
        print("Access Denied! Try again!")