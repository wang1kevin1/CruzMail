DROP DATABASE IF EXISTS cruzmail;
CREATE DATABASE IF NOT EXISTS cruzmail CHARACTER SET utf8;
USE cruzmail;

DROP TABLE IF EXISTS mailstops_master,
                     people_master,
                     packages_master;

CREATE TABLE mailstops_master (
  mailstop VARCHAR(20) NOT NULL,
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
  pkg_tracking VARCHAR(20) NOT NULL,
  name VARCHAR(20) NOT NULL,
  mailstop VARCHAR(20) NOT NULL,
  pkg_status ENUM('received','delivered') NOT NULL,
  pkg_sign ENUM('yes','no') NOT NULL DEFAULT 'no',
  pkg_email ENUM('yes','no') NOT NULL DEFAULT 'yes',
  pkg_weight ENUM('1 to 5','6 to 15','over 16'),
  pkg_date_rec DATE NOT NULL,
  pkg_date_del DATE NOT NULL,
  pkg_remarks VARCHAR(144),
  FOREIGN KEY (name) REFERENCES people_master(name) ON UPDATE CASCADE,
  FOREIGN KEY (mailstop) REFERENCES mailstops_master(mailstop) ON UPDATE CASCADE,
  PRIMARY KEY (pkg_tracking)
);
