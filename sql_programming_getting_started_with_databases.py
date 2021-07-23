# -*- coding: utf-8 -*-
"""SQL Programming - Getting Started with Databases

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sa6eXSvBs9sHGQ5i_Iq7S3cDTUTmB0fD

<font color="green">*To start working on this notebook, or any other notebook that we will use in the Moringa Data Science Course, we will need to save our own copy of it. We can do this by clicking File > Save a Copy in Drive. We will then be able to make edits to our own copy of this notebook.*</font>

# SQL Programming - Getting Started with Databases

## 1.1 Overview

Structured Query Language (SQL) is the language that is used to store, manipulate and retrieve data from many databases. It is the standard language for many relational database management systems which are a type of databases used by organisations across the world. These type of relational database management systems are used to store data in tables and examples of such include SQLite, MySQL, Postgres, Oracle etc. 

During the Moringa DataScience Prep, we will learn about SQL since as Data Scientists, we may be required to interact with this data through the use of SQL.

In this notebook, we will use SQL to learn how tables in databases are created. More specifically, we will learn how the structure of tables is defined which is critical in determining the quality of data. The better the structure, the easier it becomes to clean data.

## 1.2 Connecting to our Database
"""

# Commented out IPython magic to ensure Python compatibility.
# We will first load an sql extension into our environment
# This extension will allow us to work with sql on Colaboratory
#
# %load_ext sql

# We will then connect to our in memory sqlite database
# NB: This database will cease to exist as soon as the database connection is closed.
# We will learn more about how databases are created later in prep.
#
# %sql sqlite://

"""## 1.3 Creating a Table"""

# Commented out IPython magic to ensure Python compatibility.
# # Example 1
# # We will now define and create a table Classmates in our database (if it doesn't exist).
# # This table will have fields: PersonID, LastName, FirstName, Phone and Residence as shown below.
# # We will then fetch all records from the table.
# #
# %%sql 
# CREATE TABLE if not exists Classmates (
#     PersonID, 
#     LastName, 
#     FirstName, 
#     Phone, 
#     Residence
# ); 
# 
# SELECT * From Classmates;

# Commented out IPython magic to ensure Python compatibility.
# # Example 2
# # In this example, we will create a table named Customers 
# # with the columns Id, Name, Age, Address, Salary. 
# # This kind of a table structure can be used by Sacco Management system.
# # Then later fetch all records in the table.
# # 
# %%sql
# CREATE TABLE if not exists Customers(
#    Id,   
#    Name,  
#    Age,
#    Address,  
#    Salary
# );
# 
# SELECT * From Customers;

# Commented out IPython magic to ensure Python compatibility.
# # Example 3
# # In this example, we will create a Students table for a student management system.
# # This will contain the following fields,
# # AdmissionsNo, FirstName, MiddleName, LastName, DateOfBirth and DateOfAdmission.
# # Then fetch all records from Students table.
# #
# %%sql
# CREATE TABLE if not exists Students(
#     AdmissionsNo,
#     FirstName,
#     MiddleName,
#     LastName,
#     DateOfBirth,
#     DateOfAdmission
# );
#  
# SELECT * from Students;

"""### <font color="green"> 1.3 Challenges</font>"""

# Commented out IPython magic to ensure Python compatibility.
# # Challenge 1
# # Let us create a table name PC with the following fields; 
# # Code, model, speed, RAM, HD, CD and Price.
# # We also specify the appropriate data types to our table, then display it.
# %%sql
# CREATE TABLE if not exists  PC(
#   code,
#   module,
#   speed,
#   RAM,
#   HD,
#   CD,
#   Price
# );
# SELECT * from PC

# Commented out IPython magic to ensure Python compatibility.
# # Challenge 2
# # Let us create a table named Printer with 
# # the following code, model, speed, type and Price.
# #
# %%sql
# CREATE TABLE IF NOT EXISTS printer(
#   code,
#   model,
#   speed,
#   type,
#   price
# );
# SELECT * from printer

"""## 1.4 Specifying Column Data Types"""

# Commented out IPython magic to ensure Python compatibility.
# # Example 1
# # While defining our table, we should specify different data types. 
# # These datatypes will ensure that the particular column stores only
# # records of that type i.e. The NationalID column in the defined Citizens table 
# # below will only take integer values. These are values between  -2,147,483,648 to 2,147,483,647.
# # If one would require to store much smaller or bigger values than the range above then
# # they can use a different datatype i.e. tinyint or bigint.
# # The datatype varchar will hold letters and numbers upto the specified limit
# # in the brackets.
# #
# %%sql
# CREATE TABLE IF NOT EXISTS Citizens (
#     NationalID int,
#     FirstName varchar(255),
#     MiddleName varchar(255),
#     PostalAddress varchar(255),
#     Residence varchar(255));
# SELECT * from Citizens;

# Commented out IPython magic to ensure Python compatibility.
# # Example 2
# # Specifying column data types will ensure that 
# # the data that is stored within that table of the correct type.
# # The data type date would ensure that the data stored is in the format YYYY-MM-DD.	
# # The data type boolean supports the storage of two values: TRUE or FALSE.
# # No other data of a different nature would be accepted to the table 
# # than the one it was specified to have.
# #
# %%sql
# CREATE TABLE IF NOT EXISTS artists(
#     Artist_Id int,
#     Artist_Name varchar(60),
#     Artist_DOB date,
#     Posters_In_Stock boolean);
# 
# SELECT * from artists;

# Commented out IPython magic to ensure Python compatibility.
# # Example 3
# # The data type text accepts upto 2,147,483,647 characters
# # The data type float accepts floating point numbers i.e 183.3 as shown
# # 
# %%sql
# CREATE TABLE IF NOT EXISTS Players (
#     id int,
#     name text,
#     age integer,
#     height float);
# 
# SELECT * from Players;

"""### <font color="green"> 1.4 Challenges</font>"""

# Commented out IPython magic to ensure Python compatibility.
# # Challenge 1
# # Let's create a table customer with CustID with datatype Integer, LastName 
# # with datatype character(25), FirstName with datatype Character(20)
# #
# %%sql
# CREATE TABLE IF NOT EXISTS customer(
#   custID int,
#   lastname varchar(26),
#   firstname varchar(21)
# );
# SELECT * from customer;

# Commented out IPython magic to ensure Python compatibility.
# # Challenge 3
# # Create a table called sales that stores sales ID, customer ID, name, and address information.
# # using also the appropriate data types
# # 
# %%sql
# CREATE TABLE IF NOT EXISTS sales(
#   salesID int,
#   customerID int,
#   name varchar(15),
#   adress float
# );
# SELECT * from sales

# Commented out IPython magic to ensure Python compatibility.
# # Challenge 4
# # Create a table called employees that stores employee number, employee name, 
# # department, and salary information using appropriate data types
# #
# %%sql
# CREATE TABLE IF NOT EXISTS employees(
#   number int,
#   name varchar(15),
#   department boolean,
#   salary float
# );
# SELECT * from employees

"""## 1.5 Specifying Column Default Values"""

# Commented out IPython magic to ensure Python compatibility.
# # Example 1
# # To specify column default values, let's define a table named artists 
# # which contains three columns artist_id, artist_name and place_of_birth. 
# # - artist_id will be of the type int
# # - artist_name of the type varchar(60) 
# # - place_of_birth varchar(60) with default 'Unknown'.
# # NB: Changing the case of our data type definition will not have any effect.
# #
# %%sql 
# CREATE TABLE Artists(
#     artistid int, 
#     artistname VARCHAR(60), 
#     placeofbirth VARCHAR(60)
# );
# SELECT * from Artists

# Commented out IPython magic to ensure Python compatibility.
# # Example 2
# # To specify default values for the fields in a new table TeamMembers,
# # We do the following as shown below.
# # 
# %%sql
# CREATE TABLE IF NOT EXISTS TeamMembers (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER DEFAULT 'Unknown',
#     height REAL);
# 
# SELECT * from TeamMembers

"""### <font color="green"> 1.5 Challenges</font>"""

# Challenge 1
# Let's create a new table called latest_players with similar fields to
# the already created Players table but specify the default value to unknown
#
OUR CODE GOES HERE

# Challenge 2
# Let's create a new table called restaurants with the fields
# - name: string
# - description: text 
# - address: string, default value is unknown
# - user_id: integer
# - last_orders_at: date
# We can perform data type external research if need be
#
OUR CODE GOES HERE

"""## 1.6 Altering SQL Tables"""

# Commented out IPython magic to ensure Python compatibility.
# # Example 1: Adding a Column
# # To add a column Gender to the Classmates table, we do the following, 
# # then preview the table to see the changes
# #
# %%sql 
# ALTER TABLE Classmates ADD Gender;
#  
# SELECT * FROM Classmates;

# Commented out IPython magic to ensure Python compatibility.
# # Example 2: Deleting a Column
# # To delete a column Phone in a table above we do the following,
# # Then fetch records from the table to confirm the changes
# #
# %%sql 
# ALTER TABLE Classmates DROP Column Residence;
# SELECT * from Classmates

# Commented out IPython magic to ensure Python compatibility.
# # Example 3
# # We can change the name of the Classmates table to Schoolmates by doing the following,
# # Then fetching the records from the table to confirm the changes
# #
# %%sql  
# ALTER TABLE Classmates RENAME TO Schoolmates;
# 
# SELECT * FROM Schoolmates;

"""### <font color="green"> 1.6 Challenges</font>"""

# Commented out IPython magic to ensure Python compatibility.
# # Challenge 1
# # We can add a column DOB with the data type DATE to the TeamMembers table by;
# # Hint: The data type comes after the column name
# %%sql
# ALTER TABLE TeamMembers ADD DOB;
# SELECT * from TeamMates;

# Commented out IPython magic to ensure Python compatibility.
# # Example 4: Confirmation
# # Let's check our data type
# %%sql
# PRAGMA table_info(TeamMembers);
# SELECT DATA_TYPE from TeamMembers;

# Challenge 2
# Let's now add a column STUDIO with the data type TEXT to the Artists

"""## 1.7 Dropping SQL Tables

### 1.71 Truncating a Table
"""

# Commented out IPython magic to ensure Python compatibility.
# # Example 1
# # We may have two options while thinking about dropping (deleting) database tables. 
# # These are truncating or dropping.
# # We can use the TRUNCATE TABLE statement to delete the data inside 
# # our table as shown below. Do note that this command retains the table itself.
# # We will get to confirm the effect of using this command later when we get 
# # to insert data to the table.
# #TABLE
# %%sql TRUNCATE TABLE Classmates;

"""### 1.72 Dropping a Table"""

# Commented out IPython magic to ensure Python compatibility.
# Example 1
# We can drop our table by using the DROP TABLE statement as shown below
#
# %sql DROP TABLE Classmates;

"""### <font color="green"> 1.7 Challenges</font>"""

# Challenge 1
# Lets drop the Players table from our database
#
OUR CODE GOES HERE

# Challenge 2
# Lets drop the Customers table from our database 
#
OUR CODE GOES HERE

# Challenge 3
# And finally truncate and drop our Artists table from our database
#
OUR CODE GOES HERE