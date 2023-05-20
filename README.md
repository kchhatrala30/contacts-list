# contacts-list

From a contacts list database, you can view all contacts, search for a contact, enter a new contact or delete a contact by entering a specified command. Each contact contains a first name, last name, phone number and email address.

<li>To view all contacts, enter "V". Each contact will be displayed in a set of parenthesis with all associated data separated by commas
<li>To search for a contact, enter "S", and enter any characteristic to search by. All contacts with any field matching the entered data will be displayed
<li>To enter a new contact, enter "N", and enter the contact's first name, last name, phone number and email address. A new contact will be created using the given data and stored in the database
<li>To delete a contact, enter "D", and enter the contact's first name and last name. The contact associated with that name will be deleted from the database

This project uses Python and a MySQL connector to connect with a database which stores the contacts and is queried through user input. It was originally created in Nov 2022 using Visual Studio 2022, but was moved to Visual Studio Code.

Keep track of your contacts with a few simple commands!
