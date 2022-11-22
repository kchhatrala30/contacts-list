import mysql.connector
import time

dbase = mysql.connector.connect(host="localhost", user="root", passwd="IloveUNCC*0!", database="contactbook")
cursor = dbase.cursor()

#cursor.execute("CREATE TABLE Person (FirstName CHAR(20), LastName CHAR(20), PhoneNum CHAR(10), Email CHAR(30))")

xFlag = True
while xFlag:
    print("---Contact List---")
    print("What would you like to do?")
    print("\tView all contacts: V")
    print("\tEnter new contact: E")
    print("\tDelete contact: D")
    print("\tExit the contact list: X")
    choice = input("Select your option: ")
    print()

    if choice == "V":
        cursor.execute("SELECT * FROM person;")
        for i in cursor:
            print(i)

    elif choice == "E":
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
