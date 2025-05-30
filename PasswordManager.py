from Tools import *
import random
from random import shuffle
import pandas as pd
credentials = False
tries = 0
accounts = pd.read_csv("accounts.csv")

def intialUserLogin(credentials):
    existingUser = input("Do you have an account? (y/n)")
    
    if existingUser == "y":
        userUser = input("What is your username? ")
        for i in range(len(accounts["username"])):
            if userUser == accounts["username"][i]:
                username = accounts["username"][i]
                password = accounts["password"][i]
                hint = accounts["hint"][i]
                # print(accounts["password"][i])
        # print(hint)
    else:
        print("Create a Profile:")
        category, name, username, password, hint = Account.newAccount()
        accounts.loc[len(accounts)] = [category, name, username, password, hint]
        accounts.to_csv("accounts.csv", index=False)
        
    tries=0
    userUser=""
    userPass=""
    while credentials != True:
        if tries <3:
            if userUser==username and userPass==password:  #however you check if the credentials are correct
                credentials = True
            else:
                userUser = input("Username:  ")
                print(f"Password Hint: {hint}")  # Access the hint from the text file and print to screen
                userPass = input("Password:  ")
                if userUser!=username and userPass!=password:
                    tries+=1
                if tries>0:
                    print("Incorrect username or password, try again")
        else:
            print("Sorry, you have too many invalid login attempts. Close the program and try again.")
            exit()

def invalid_choice():
    print("Invalid choice. Please select a valid option.")

def exit():
    print("Goodbye!")
    raise SystemExit  #stops the program

# MAIN LOOP

options = {
        "1":Account.newAccount,
        "2":Account.viewAccount,
        "3":Account.viewByCategory,
        "4":Passwords.passwordGenerator,
        "5":Account.changeAccount,
        "6":Account.deleteAccount,
        "7":exit
        }

#Login
# intialUserLogin(False)

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