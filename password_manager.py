
# for this program, since it contains passwords that are sensitive therefore it needs a master password to access it and for authicating this master 
# password we use the hash library.

import hashlib

try:
    stored_pass = open('master.txt', 'r').read()    # opening the file that contains the hashed master password

except FileNotFoundError:                           # if the user has not set the master password yet 
    print("No master password found")
    master_password = input("Set your master password: ")
    hashed_master = hashlib.sha256(master_password.encode()).hexdigest()
    with open('master.txt', 'w') as f:
        f.write(hashed_master)
    print("Master password set successfully!")
    stored_pass = hashed_master


master_password= input("Enter the master password:")            # user is prompter to enter the master password 
if hashlib.sha256(master_password.encode()).hexdigest() != stored_pass:
    print("Incorrect master password! Exiting...")                  # if the password entered by the user does not match the hased password stored in the file 
    quit()
else:
    print("Access granted!")                # if the user entered the correct master password 

<<<<<<< HEAD
def view():                                # function to view the passwords which are saved in the txt file 
    with open('passwords.txt', 'r') as f:
=======
def view():
    with open('passwords.txt', 'r') as f:               # function to view the stored passwords 
>>>>>>> 3c406d9 (Added master password authication using hashing and updated comments)
        for line in f.readlines():
            data = line.rstrip() 
            user, passw = data.split("|")
            print("User: " + user + " |" + " Password: " + passw)

def add():                                            # function to add a username as well as its respective password to the txt file 
    with open('passwords.txt', 'a') as f:
        user_name = input("Enter the username: ")               # function to add a new password 
        pwd = input("Enter the password: ")
        f.write(user_name + "|" + pwd + "\n")
        print("Password added successfully!")

while True:
    print("Welcome to the Password Manager!")
    print("Please see the below options and type the corresponding number to proceed:")
    print("1.View the stored passwords")                                                    # showing the different options a user can choose from in the program 
    print("2.Add a new password")
    print("3.Exit the Password Manager")
    choice = int(input("Please enter your choice: "))

<<<<<<< HEAD
    if choice == 1:                                            # when user wants to view the passwords 
        print("Here are your stored passwords:")
        view()
        pass

    if choice == 2:                        # when user wants to add the passwords 
        add()
        pass

    if choice == 3:                                                                   # when user wants to exit the program 
        print("Exiting the Password Manager. Goodbye!")
=======
    if choice == 1:
        print("Here are your stored passwords:")                # if the user wants to view the stored passwords then the view function is called 
        view()
        pass

    if choice == 2:         # if the user wants to add a new password then the add function is called
        add()
        pass

    if choice == 3:
        print("Exiting the Password Manager. Goodbye!")             # if the user wants to exit the program
>>>>>>> 3c406d9 (Added master password authication using hashing and updated comments)
        break


    

