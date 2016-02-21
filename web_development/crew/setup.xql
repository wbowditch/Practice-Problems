CREATE TABLE club (
name VARCHAR(40),
email VARCHAR(50), 
password CHAR(40), 
registration_date datetime, 
membership_type enum('coxswain', 'starboard', 'port') 
);
