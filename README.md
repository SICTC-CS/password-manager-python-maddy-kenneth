[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/CP6FLelp)
# Password Manager:


### i. Products to include:

1.  **Log in to run the program:**
    * Include a hint.
    * Limit the number of login attempts to 3 before the program shuts down.
    * If the user is a first-time user, allow them to create a profile.
        * Profile requirements: username, password (password requirements in item h), first, and last name.
        * Require users to log in after registration.
2.  **Method to take in user input to store Account(username, password) based on categories.**
    * Accounts must be able to be pulled based on categories.
    * Each account needs the following data:
        * Name
        * Username
        * Password
        * Category
3.  **Utilize a text file as a database:**
    * Allow users to access their passwords again later.
    * Users should be able to close down the program and log back in.
4.  **Navigation through user-created categories:**
    * Examples of categories: home, work, entertainment, bills, etc.
    * Should be able to print out the categories for the user to view them.
5.  **Password generator option (same as homework assignment):**
    * Half points: include in a method.
    * Full points: setup as a static method in a separate class.
6.  **Delete or modify Account details.**
7.  **Simple output format:**
    ```
    The account: {accountName}
    The username: {username}
    The password: {password}
    ```
8.  **User input and generated password requirements:**
    * 1 capital character.
    * 1 number.
    * 1 special character (certain special characters allowed).
    * At least 8 characters long.
    * Half points: create a method to check this.
    * Full points: create a class to check this.
9.  **10% Bonus:** Save the file as a password-protected or encrypted file.
10. **5% Bonus:** Create a method to check brute-force break time.
11. **15% Bonus:** Save the info on an actual database.

### ii. Computer Science concepts to include:

1.  User Input.
2.  Lists.
3.  Utilizing built-in functions for password creation (not a list of characters).
4.  Loops.
5.  All methods are commented.
6.  Multiple Classes (Suggestions: Account, Library, OpenCloseFile, etc.)
    * The user should not be able to create a runtime error.
    * The usability of the program should be smooth and easy to understand.
    * Remember that each section of code needs to be commented, and any outside sources need to be documented.
    * MUST HAVE a design overview when submitting your final version.
        * Include features, implementation details, and who is doing which features.
    * Example password manager: [KeePass](https://sourceforge.net/projects/keepass/files/KeePass%202.x/2.52/KeePass-2.52-Setup.exe/download)

## Recommendations:

* Utilize starter code from notes (course registration, CSE 322, CSE 324).
* Split up the work and compile the code into a simple main loop with conditional statements for different features.
* Use a class (makes things easier).
* Comment your code.
* Get code review time before the due date.
* Encryption: Not saved in plain text and difficult to break.
