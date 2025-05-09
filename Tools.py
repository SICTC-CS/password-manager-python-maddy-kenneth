from random import shuffle
import random
special = ["!","@","#","$","%","^","&","*","(",")"]

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
    
    
    def viewAccount(accounts, whichAcc):
        
        for i in range(len(accounts,name,username,password)):
            category,name,username,password,hint = accounts[i].strip().split(",")
            if whichAcc == name:
                print(f'''
                        The account: {name}
                        The username: {username}
                        The password: {password}
                        ''')
                
                
    def viewByCategory(accounts):
        #print out the categories that they can filter by
        #obtain which category to filter by
        whichCat = input("Which category do you want to filter by?  ")

        filtered = accounts[accounts['whichCat'].str.low() == whichCat.lower()]
        
        print(f'Accounts under category {whichCat}')
        for name in filtered['name']:
            print(name)
            
    
    def newAccount():
        category = input("Category (Home, Work, Entertainment, Bills): ")
        name = input("Account Name: ")
        username = input("Username: ")
        password = input("Password: ")   # Make sure the password meets requirements
        hint = input("Password Hint: ")
        return category, name, username, password, hint
        
        
    def changeAccount(accounts):
        whichAcc = input("Which account would you like to Change?  ")
        
        #viewAccount()  Run the viewAccount function to show them the current stored information

        #get data that they want to change

        #read in all the data aka save the file to a list
       
        #find the old account
        for i in range(len(accounts)):
            category,name,username,password,hint = accounts[i].strip().split(",")
            # Need to add something else to make this actually work


    def deleteAccount(accounts):
        whichAcc = input("Which account would you like to delete?  ")
        newLines = []
        found = False
        
        with open("accounts.csv","r") as file:
            lines = file.readlines() #converts file to list
        for i in range(len(lines)):
            category,name,username,password,hint = accounts[i].strip().split(",")
            if whichAcc != name:
                newLines.append(i)
            else: 
                found = True
                
        #Tell them if the account is not found
        if not found:
            print("The account was not found.")
            return
        
        with open("accounts.csv","r") as file:
            file.writelines(newLines)
            
                        