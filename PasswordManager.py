import random
from random import shuffle
credentials = False
tries = 0


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
        userUser = input("Username:  ")
        userPass = input("Password:  ")
    else:
        print("Create a Profile:")
        username = input("Username: ")
        password = input("Password: ")   # Make sure the password meets requirements
        hint = input("Password Hint: ")
        first = input("First Name: ")
        last = input("Last Name: ")
        
    tries=0
    if tries <3:
        userUser=""
        userPass=""
        while credentials != True:
            if userUser==username and userPass==password:  #however you check if the credentials are correct
                credentials = True
            else:
                if tries>0:
                    print("Incorrect username or password, try again")
                userUser = input("Username:  ")
                print(f"Password Hint: ______")  # Access the hint from the text file and print to screen
                userPass = input("Password:  ")
                tries+=1
    else:
        print("Sorry, you have too many invalid login attempts. Close the program and try again.")
        exit()


def newAccount():
    category = input("Category (Home, Work, Entertainment, Bills): ")
    name = input("Account Name: ")
    username = input("Username: ")
    password = input("Password: ")   # Make sure the password meets requirements
    hint = input("Password Hint: ")
    
    with open("accounts.csv","a") as file:
        lineToWrite = f"{category},{name},{username},{password},{hint}\n"
        file.write(lineToWrite)
        print(f"{name} was added!")


def viewByCategory():
    #print out the categories that they can filter by
    #obtain which category to filter by
    whichCat = input("Which category do you want to filter by?  ")

    #read the data and save to a list
    with open("accounts.csv","r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        category,name,username,password,hint = lines[i].strip().split(",")
    
        if whichCat == category:
            print(name)   #Print the account name


def viewAccount():
    whichAcc = input("Which account would you like to change?  ")
    
    with open("accounts.csv","r") as file:
        lines = file.readlines() #converts file to list
    for i in range(len(lines)):
        category,name,username,password,hint = lines[i].strip().split(",")
        if whichAcc == name:
           print(f'''
                 The account: {name}
                 The username: {username}
                 The password: {password}
                 ''')


def changeAccount():
    whichAcc = input("Which account would you like to delete?  ")
    
    #viewAccount()  Run the viewAccount function to show them the current stored information

    #get data that they want to change

    with open("accounts.csv","r") as file:
        lines = file.readlines() #converts file to list
    #find the old account
    for i in range(len(lines)):
        category,name,username,password,hint = lines[i].strip().split(",")  # Will this work with more than 2 variables?
        if name == old:
            name = new
            newData = f"{category},{name},{username},{password},{hint}\n"
            lines[i] = newData
    print(lines) 
    #overwrite the file
    with open("accounts.csv","w") as file:
        for eachLine in lines:
            file.write(eachLine)



def deleteAccount():
    whichAcc = input("Which account would you like to delete?  ")
    newLines = []
    found = False
    with open("accounts.csv","r") as file:
        lines = file.readlines() #converts file to list
    for i in range(len(lines)):
        category,name,username,password,hint = lines[i].strip().split(",")
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
           


def invalid_choice():
    print("Invalid choice. Please select a valid option.")

def exit():
    print("Goodbye!")
    raise SystemExit  #stops the program




# MAIN LOOP

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