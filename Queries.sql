USE CONTACTBOOK;

# Table Data: FirstName char(20), LastName char(20), PhoneNum char(15), Email char(30)

# View Contacts Tester
SELECT * FROM person;

# Search for Contact Tester
SELECT * FROM person where FirstName LIKE "%d@te%" OR LastName LIKE "%d@te%" OR PhoneNum LIKE "%d@te%" OR Email LIKE "%d@te%";

# Add Contacts Tester
INSERT INTO person VALUES("TestFirst", "Test01", "1234567890", "first@test.com");
INSERT INTO person VALUES("TestSecond", "Test02", "0987654321", "second@test.com");
INSERT INTO person VALUES("TestThird", "Test03", "0123456789", "third@test.com");

# Delete Contacts Tester
DELETE FROM person WHERE FirstName = "TestSecond" AND LastName = "Test02";

# Clear Table for Testing
DELETE FROM person;