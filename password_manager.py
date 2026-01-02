master_password= input("Enter the master password:")


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line)

def add():
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

    if choice == 1:
        print("Here are your stored passwords:")
        view()
        pass

    if choice == 2:
        add()
        pass

    if choice == 3:
        print("Exiting the Password Manager. Goodbye!")
        break


    

