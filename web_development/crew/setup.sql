CREATE TABLE club (
name VARCHAR(40),
email VARCHAR(50), 
password CHAR(40), 
registration_date datetime, 
membership_type enum('coxswain', 'starboard', 'port') 
);

INSERT INTO club VALUES ('Will Bowditch', 'bowditcw@bc.edu', sha1('password1'),now(),'coxswain');

INSERT INTO club VALUES ('Bob Smith', 'bobsmith@bc.edu', sha1('password2'),now(),'starboard');

INSERT INTO club VALUES ('Fred Williams', 'fredwilliams@bc.edu', sha1('password3'),now(),'port');

UPDATE club SET email='william.bowdith@bc.edu' WHERE name='Will Bowditch';

DELETE FROM club WHERE name='Bob Smith';

