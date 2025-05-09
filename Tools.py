import pandas as pd
from random import shuffle
import random
special = ["!","@","#","$","%","^","&","*","(",")"]
accounts = pd.read_csv("accounts.csv")

class Passwords:
        
    def passwordGenerator():
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

        word = list(password)
        shuffle(word)
        return ''.join(word)
    
    def passwordValidator(password):
        hasUpper=False
        hasLower=False
        hasDigit=False
        hasSpecial=False
        
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        
        #Check for the characters
        for char in password:
            if char.isupper():
                hasUpper = True
            elif char.islower():
                hasLower = True
            elif char.isdigit():
                hasDigit = True
            elif char in special:
                hasSpecial = True
        
        #Return a corresponding message if one test fails
        if not hasUpper:
            return False, "Password needs at least one uppercase letter"
        if not hasLower:
            return False, "Password needs at least one lowercase letter"
        if not hasDigit:
            return False, "Password needs at least one digit"
        if not hasSpecial:
            return False, "Password needs at least one special character"
        
        return True, "Password passes all tests!"
    

class Account:
    def __init__(self, filename="accounts.csv"):
        self.filename = filename
    
    def viewAccount():
        whichAcc = input("Which account would you like to Change?  ")
        for i in range(len(accounts["category"])):
            if accounts["username"][i] == whichAcc:
                category = accounts["category"][i]
                name = accounts["name"][i]
                username = accounts["username"][i]
                password = accounts["password"][i]
                hint = accounts["hint"][i]
                break
        
        print(f'''
              category: {category}
              name: {name}
              user: {username}
              password: {password}
              hint: {hint}''')
        
        return whichAcc
                
    def viewByCategory():
        #print out the categories that they can filter by
        #obtain which category to filter by
        whichCat = input("Which category do you want to filter by?  ")

        for i in range(len(accounts["category"])):
            if accounts["category"][i] == whichCat:
                print(f'''
    Category: {accounts["category"][i]}
    Name: {accounts["name"][i]}
    Username: {accounts["username"][i]}
    Password: {accounts["password"][i]}
    hint: {accounts["hint"][i]}''')
            
    
    def newAccount():
        category = input("Category (Home, Work, Entertainment, Bills): ")
        name = input("Account Name: ")
        username = input("Username: ")
        password = input("Password: ")   # Make sure the password meets requirements
        valid, message = Passwords.passwordValidator(password)
        print(message)
        while not valid:
            password = input("Password: ")
            valid, message = Passwords.passwordValidator(password)
            print(message)
        hint = input("Password Hint: ")
        return category, name, username, password, hint
        
        
    def changeAccount():
        whichAcc = Account.viewAccount() #Run the viewAccount function to show them the current stored information

        #get data that they want to change
        whichPart = input(f"which part of {whichAcc} do you want to change? ")
        for i in range(len(accounts["username"])):
            if whichAcc == accounts["username"][i]:
                whichPart.lower()
                accounts[whichPart][i] = input("What do you want to change it to? ")
                category = accounts["category"][i]
                name = accounts["name"][i]
                username = accounts["username"][i]
                password = accounts["password"][i]
                hint = accounts["hint"][i]
                break
        
        #read in all the data aka save the file to a list
        accounts.to_csv("accounts.csv", index=False)
        #find the old account
        # for i in range(len(accounts)):
        #     category,name,username,password,hint = accounts[i].strip().split(",")
        #     # Need to add something else to make this actually work


    def deleteAccount():
        whichAcc = input("Which account would you like to delete?  ")
        
        for i in range(len(accounts["username"])):
            if whichAcc == accounts["username"][i]:
                found = i
                
        accounts.drop(i)
        print(accounts)
        accounts.to_csv("accounts.csv", index=False)