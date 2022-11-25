import mysql.connector
import time

dbase = mysql.connector.connect(host="localhost", user="root", passwd="CLASSIFIED", database="contactbook")
cursor = dbase.cursor()

xFlag = True
while xFlag:
    print("---Contact List---")
    print("What would you like to do?")
    print("\tView all contacts: V")
    print("\tSearch for a contact: S")
    print("\tEnter new contact: N")
    print("\tDelete contact: D")
    print("\tExit the contact list: X")
    choice = input("Select your option: ")
    print()

    if choice == "V":
        cursor.execute("SELECT * FROM person")
        for i in cursor:
            print(i)

    elif choice == "S":
        searchBy = input("Enter info about the contact: ")
        searchBy = "%" + searchBy + "%"
        toSearch = (searchBy, searchBy, searchBy, searchBy)
        cursor.execute("SELECT * FROM person WHERE FirstName LIKE %s OR LastName LIKE %s OR PhoneNum LIKE %s OR Email LIKE %s", toSearch)
        for i in cursor:
            print(i)

    elif choice == "N":
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        phoneNum = input("Enter phone number: ")
        email = input("Enter email: ")

        toAdd = (firstName, lastName, phoneNum, email)
        cursor.execute("INSERT INTO person VALUES(%s, %s, %s, %s)", toAdd)
        dbase.commit()
        print("Contact for", firstName, lastName, "has been added successfully")

    elif choice == "D":
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        
        cursor.execute("DELETE FROM person WHERE FirstName = \"" + firstName + "\" AND LastName = \"" + lastName + "\"")
        dbase.commit()
        print("Contact for", firstName, lastName, "has been deleted successfully")

    elif choice == "X":
        xFlag = False
        exit()

    print()
    time.sleep(1)
