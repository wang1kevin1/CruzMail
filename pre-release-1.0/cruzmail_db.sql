# To manually create/use a database:
# usage: terminal/command line
# create a database:
# type: 'mysql -u root' to launch mysql terminal
# CREATE DATABASE db_name;
# You can type 'show databases;' to make sure your db has been successfully created.
# mysql -u root -A db_name < cruzmail_db.sql
# Make sure you are using the correct database.
# Type 'USE db_name;' to use the right db.
#
# May have to edit a configuration file in Django to connect to this database.

CREATE TABLE mailstops_master (
  mailstop VARCHAR(50) NOT NULL DEFAULT  '',
  ms_name VARCHAR(50) NOT NULL DEFAULT '',
  ms_route_order VARCHAR(3) NOT NULL DEFAULT '',
  ms_route ENUM('W','C','E') NOT NULL NOT NULL DEFAULT  'W',
  ms_status ENUM('active','inactive') NOT NULL DEFAULT 'active',
  PRIMARY KEY (mailstop)
);

CREATE TABLE people_master (
  name VARCHAR(50) NOT NULL DEFAULT '',
  email VARCHAR(50) NOT NULL DEFAULT '',
  mailstop VARCHAR(50) NOT NULL DEFAULT '',
  PRIMARY KEY (email)
);

CREATE TABLE packages_master (
  pkg_tracking VARCHAR(32) NOT NULL DEFAULT '',
  name VARCHAR(50) NOT NULL DEFAULT '',
  mailstop VARCHAR(50) NOT NULL DEFAULT '',
  pkg_status ENUM('received','delivered') NOT NULL DEFAULT 'received',
  pkg_sign ENUM('yes','no') NOT NULL DEFAULT 'no' DEFAULT 'no',
  pkg_email ENUM('yes','no') NOT NULL DEFAULT 'yes' DEFAULT 'yes',
  pkg_weight ENUM('1 to 5','6 to 15','over 16') DEFAULT '1 to 5',
  pkg_date_rec DATE NOT NULL DEFAULT NOW(),
  pkg_date_del DATE,
  pkg_remarks VARCHAR(144),
  PRIMARY KEY (pkg_tracking)
);
