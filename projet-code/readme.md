
# CSI4142 Project - Readme

 Our team was tasked with building a data mart using the ETL (Extraction, Transformation, and Loading) process. The data was extracted from a CSV file and transformed by handling missing values, removing duplicates, and converting data types. The transformed data was then loaded into a database management system (DBMS) of our choice. In this project, we used PostgreSQL as our DBMS.

## Files

* create-table.py: This script creates the necessary table in the database to store the data.
* insert-table.py: This script imports the CSV file into the database and performs data insertion.
* Dataset.csv: This file contains the data to be imported into the database.
* readme.md: This file provides an overview of the project and the files included.

## Usage

1. Ensure that PostgreSQL is installed on your system and that you have the necessary credentials to access the database.
2. Run the `create-table.py` script to create the necessary table in the database.
3. Update the `insert-table.py` script with your database credentials.
4. Run the `insert-table.py` script to import the data from the CSV file into the database.

## Dependencies

* Python
* psycopg2 Python library
