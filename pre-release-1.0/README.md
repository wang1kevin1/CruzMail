# Setup Guide

## Setting Up the WebApp: cruzmail/~

### Installing Django

stuff

### Testing the WebApp

stuff



## Setting Up the Database: db_build.sql

### Prerequisites
* UNIX based server environment

### Installing the MySQL Environment

Install the MySQL server using the package installer:
```
$ sudo apt-get update
$ sudo apt-get install mysql-server
$ sudo mysql_secure_installation
```

Allow remote access:
```
$ sudo ufw allow mysql
```

Start the MySQL service and enable it to launch at reboot:
```
$ sudo systemctl start mysql
$ sudo systemctl enable mysql
```

Start the MySQL shell:
```
$ sudo mysql -u root -p
```

### Creating the Database

Download cruzmail_db.sql. Change directory to its location and run:
```
$ sudo mysql < cruzmail_db.sql
```

### Testing the Installation

After installing the database, you can display output in table format as such:
```
$ sudo mysql -t < cruzmail_db.sql
```