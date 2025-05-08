from Tools import *
import random
from random import shuffle
import pandas as pd
credentials = False
tries = 0
accounts = pd.read_csv("accounts.csv")


def invalid_choice():
    print("Invalid choice. Please select a valid option.")

def exit():
    print("Goodbye!")
    raise SystemExit  #stops the program

def newAccount(accounts):
        category = input("Category (Home, Work, Entertainment, Bills): ")
        name = input("Account Name: ")
        username = input("Username: ")
        password = input("Password: ")   # Make sure the password meets requirements
        hint = input("Password Hint: ")
        
        listOfAccounts.append(Account(category,name,username,password,hint))
        ## Need something after this to actually write to the file    


# MAIN LOOP

options = {
        "1":newAccount,
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