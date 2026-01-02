master_password= input("Enter the master password:")


def view():                                # function to view the passwords which are saved in the txt file 
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line)

def add():                                            # function to add a username as well as its respective password to the txt file 
    with open('passwords.txt', 'a') as f:
        user_name = input("Enter the username: ")
        pwd = input("Enter the password: ")
        f.write(user_name + "|" + pwd + "\n")
        print("Password added successfully!")

while True:
    print("Welcome to the Password Manager!")
    print("Please see the below options and type the corresponding number to proceed:")
    print("1.View the stored passwords")
    print("2.Add a new password")
    print("3.Exit the Password Manager")
    choice = int(input("Please enter your choice: "))

    if choice == 1:                                            # when user wants to view the passwords 
        print("Here are your stored passwords:")
        view()
        pass

    if choice == 2:                        # when user wants to add the passwords 
        add()
        pass

    if choice == 3:                                                                   # when user wants to exit the program 
        print("Exiting the Password Manager. Goodbye!")
        break


    

