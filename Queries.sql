USE CONTACTBOOK;

# Table Data: FirstName char(20), LastName char(20), PhoneNum char(10), Email char(30)

# View Contacts Tester
SELECT * FROM person;

# Add Contacts Tester
INSERT INTO person VALUES("TestFirst", "TestLast", "1234567890", "tester@test.com");

# Delete Contacts Tester
DELETE FROM person WHERE FirstName = "TestFirst" AND LastName = "TestLast";
