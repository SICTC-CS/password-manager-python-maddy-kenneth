import random
from random import shuffle
import pandas as pd
credentials = False
tries = 0
accounts = pd.read_csv("accounts.csv")


def passwordValidator():
    pass


def passwordGenerator():
    def shuffle_password(word):  
        word = list(word)
        shuffle(word)
        return ''.join(word)

    numUpper = int(input("How many capital letters do you want in your password?  "))
    numLower = int(input("Lowercase letters?  "))
    numNumbers = int(input("Numbers?  "))
    numSpec = int(input("Special characters?  "))

    special = ["!","@","#","$","%","^","&","*","(",")"]
    password = ""

    u=1
    for u in range (1,numUpper+1):
        rand = random.randint(65,90)
        letter = chr(rand)                      
        password = password + letter
        letter = ""
    l=1
    for l in range (1,numLower+1):
        rand = random.randint(97,122)
        letter = chr(rand)
        password = password + letter
        letter = ""
    n=1
    for n in range (1,numNumbers+1):
        rand = str(random.randint(0,9))
        password = password + rand
    s=1
    for s in range (1,numNumbers+1):
        rand = random.randint(0,9)
        char = special[rand]
        password = password + char

    print(shuffle_password(password))
    return password


def intialUserLogin(credentials):
    existingUser = input("Do you have an account? (y/n)")
    
    if existingUser == "y":
        username = accounts["username"][userUser]
        password = accounts["password"][userPass]
        hint = accounts["hint"][userUser]
        print(hint)
    else:
        print("Create a Profile:")
        category = input("What type of account is this? ")
        username = input("Username: ")
        password = input("Password: ")   # Make sure the password meets requirements
        hint = input("Password Hint: ")
        first = input("First Name: ")
        last = input("Last Name: ")
        accounts.loc[len(accounts[])]
    tries=0
    userUser=""
    userPass=""
    while credentials != True:
        if tries <3:
            if userUser==username and userPass==password:  #however you check if the credentials are correct
                credentials = True
            else:
                userUser = input("Username:  ")
                print(f"Password Hint: ______")  # Access the hint from the text file and print to screen
                userPass = input("Password:  ")
                if userUser!=username and userPass!=password:
                    tries+=1
                if tries>0:
                    print("Incorrect username or password, try again")
        else:
            print("Sorry, you have too many invalid login attempts. Close the program and try again.")
            exit()

def newAccount():
    category = input("Category (Home, Work, Entertainment, Bills): ")
    name = input("Account Name: ")
    username = input("Username: ")
    password = input("Password: ")   # Make sure the password meets requirements
    hint = input("Password Hint: ")


def viewByCategory():
    #print out the categories that they can filter by
    #obtain which category to filter by
    whichCat = input("Which category do you want to filter by?  ")

    #read the data and save to a list
    


def viewAccount():
    pass


def changeAccount():
    # ask which account they want to change
    
    #viewAccount()  Run the viewAccount function to show them the current stored information

    #get data that they want to change

    #read in all the data aka save the file to a list
    #find the old account
    for i in range(len(lines)):
        category,name,username,password,hint = lines[i].strip().split(",")  # Will this work with more than 2 variables?
        if name == old:
            name = new
            newData = f"{category},{name},{username},{password},{hint}\n"
            lines[i] = newData
    print(lines) 
    #overwrite the file



def deleteAccount():
    pass


def invalid_choice():
    print("Invalid choice. Please select a valid option.")

def exit():
    print("Goodbye!")
    raise SystemExit  #stops the program




# Main Loop 

options = {
        "1":newAccount,
        "2":viewAccount,
        "3":viewByCategory,
        "4":passwordGenerator,
        "5":changeAccount,
        "6":deleteAccount,
        "7":exit
        }

#Login
intialUserLogin(False)

while True:
    print("\n--- Password Manager ---")
    print("1. Add a New Account")
    print("2. View an Account")
    print("3. Filter by Category")
    print("4. Password Generator")
    print("5. Change an Account")
    print("6. Delete an Account")
    print("7. Exit")
    choice = input("Choose an option (1-7): ").strip()
                                    
    #dictionary.getChoice and if invalid run other command                                    
    action = options.get(choice,invalid_choice)
    action()