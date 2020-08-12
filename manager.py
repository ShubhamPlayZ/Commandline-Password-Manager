import sqlite3

connection = sqlite3.connect("passwords.db")
cursor = connection.cursor()

masterPassword = "3141592"

cursor.execute('CREATE TABLE IF NOT EXISTS passwords (accounts text, password text)')
cursor.execute('SELECT * FROM passwords WHERE accounts = "masterPassword"')
connection.commit()
checker = cursor.fetchall()

if len(checker) == 0:
    cursor.execute('INSERT INTO passwords VALUES(?, ?)', ("masterPassword", masterPassword))
    connection.commit()
elif checker[0][1] != masterPassword:
    cursor.execute("UPDATE passwords SET password=? WHERE accounts='masterPassword'", (masterPassword,))

cursor.execute("SELECT * FROM passwords WHERE accounts = 'masterPassword'")
passChecker = cursor.fetchall()



while True:
    userPassInput = str(input("Enter the master password: "))
    if userPassInput == passChecker[0][1]:
        break
    else:
        print("Wrong Password")

mainloop = True

while mainloop:
    print('"A" to add \n"S" to see \n"Q" to quit program')
    userChoice = str(input())
    
    if userChoice.lower() == "q":
        mainloop = False

    elif userChoice.lower() == 'a':
        accountName = str(input("Enter account name: "))
        passwordName = str(input("Enter password: "))
        cursor.execute("INSERT INTO passwords VALUES (?, ?)", (accountName.lower(), passwordName))
        connection.commit()
    
    elif userChoice.lower() == "s":
        accountName = str(input("Enter account name: "))
        cursor.execute("SELECT * FROM passwords WHERE accounts = ?", (accountName.lower(),))
        info = cursor.fetchall()
        if len(info) > 0:
            print(f'The password is {info[0][1]}')
        else:
            print("Account doesn't exist within the database")

    else:
        print("Sorry, we dont understand that input")



