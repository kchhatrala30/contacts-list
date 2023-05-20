import mysql.connector
import time
import info

dbase = mysql.connector.connect(host=info.host, user=info.user, passwd=info.passwd, database=info.database)
cursor = dbase.cursor()

while True:
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

        toDelete = (firstName, lastName)
        cursor.execute("DELETE FROM person WHERE FirstName = %s AND LastName = %s", toDelete)
        dbase.commit()
        print("Contact for", firstName, lastName, "has been deleted successfully")

    elif choice == "X":
        break
        quit()

    elif choice == "CLEAR":
        cursor.execute("DELETE FROM person")

    elif choice == "TEST":
        cursor.execute("DELETE FROM person")
        reset1 = ("TestFirst", "Test01", "1234567890", "first@test.com")
        reset2 = ("TestSecond", "Test02", "0987654321", "second@test.com")
        reset3 = ("TestThird", "Test03", "0123456789", "third@test.com")
        cursor.execute("INSERT INTO person VALUES(%s, %s, %s, %s)", reset1)
        cursor.execute("INSERT INTO person VALUES(%s, %s, %s, %s)", reset2)
        cursor.execute("INSERT INTO person VALUES(%s, %s, %s, %s)", reset3)

    else:
        print("Invalid input. Please enter one of the following options.")
    
    print()
    time.sleep(1)
