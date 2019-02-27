# To manually create/use a database:
# usage: terminal/command line
# create a database:
# type: 'mysql -u root' to launch mysql terminal
# CREATE DATABASE db_name;
# You can type 'show databases;' to make sure your db has been successfully created.
# mysql -u root -A cruzmail < cruzmail_db.sql
# Make sure you are using the correct database.
# Type 'USE db_name;' to use the right db.
#
# Using the automatic creation of database cruzmail
# mysql -u root -A cruzmail < cruzmail_db.sql
#
# May have to edit a configuration file in Django to connect to this database.


DROP DATABASE IF EXISTS cruzmail;
CREATE DATABASE IF NOT EXISTS cruzmail CHARACTER SET utf8;
USE cruzmail;

# I think this is unnecessary.
DROP TABLE IF EXISTS mailstops_master,
                    people_master,
                    packages_master;

CREATE TABLE mailstops_master (
  mailstop VARCHAR(50) NOT NULL,
  ms_status ENUM('active','inactive') NOT NULL DEFAULT 'active',
  ms_route ENUM('West','Central','East') NOT NULL,
  PRIMARY KEY (mailstop)
);

CREATE TABLE people_master (
  name VARCHAR(20) NOT NULL,
  email VARCHAR(20) NOT NULL,
  mailstop VARCHAR(20) NOT NULL,
  FOREIGN KEY (mailstop) REFERENCES mailstops_master(mailstop) ON UPDATE CASCADE,
  PRIMARY KEY (name, mailstop)
);

CREATE TABLE packages_master (
  pkg_tracking VARCHAR(50) NOT NULL,
  name VARCHAR(50) NOT NULL,
  mailstop VARCHAR(50) NOT NULL,
  pkg_status ENUM('received','delivered') NOT NULL,
  pkg_sign ENUM('yes','no') NOT NULL DEFAULT 'no',
  pkg_email ENUM('yes','no') NOT NULL DEFAULT 'yes',
  pkg_weight ENUM('1 to 5','6 to 15','over 16'),
  pkg_date_rec DATE NOT NULL,
  pkg_date_del DATE,
  pkg_remarks VARCHAR(144),
  FOREIGN KEY (name) REFERENCES people_master(name) ON UPDATE CASCADE,
  FOREIGN KEY (mailstop) REFERENCES mailstops_master(mailstop) ON UPDATE CASCADE,
  PRIMARY KEY (pkg_tracking)
);
