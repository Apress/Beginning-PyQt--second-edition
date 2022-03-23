"""Listing 14-4 to Listing 14-7
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys, random
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class CreateEmployeeData:
    """Create sample database for project. 
    Class demonstrates how to connect to a database, create 
    queries, and create tables and records in those tables."""
    # Create connection to database. If db file does not exist, 
    # a new db file will be created.
    database = QSqlDatabase.addDatabase("QSQLITE") # SQLite version 3
    database.setDatabaseName("files/accounts.db")

    if not database.open():
        print("Unable to open data source file.")
        sys.exit(1) # Error code 1 - signifies error

    query = QSqlQuery()
    # Erase database contents
    query.exec("DROP TABLE accounts")
    query.exec("DROP TABLE countries")

    query.exec("""CREATE TABLE accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                employee_id INTEGER NOT NULL,
                first_name VARCHAR(30) NOT NULL,
                last_name VARCHAR(30) NOT NULL,
                email VARCHAR(40) NOT NULL,
                department VARCHAR(20) NOT NULL, 
                country_id VARCHAR(20) REFERENCES countries(id))""")

    # Positional binding to insert records into the database
    query.prepare("""INSERT INTO accounts (
                  employee_id, first_name, last_name, 
                  email, department, country_id) 
                  VALUES (?, ?, ?, ?, ?, ?)""")

    first_names = ["Emma", "Olivia", "Ava", "Isabella", "Sophia",
                   "Mia", "Charlotte", "Amelia", "Evelyn", "Abigail",
                    "Valorie", "Teesha", "Jazzmin", "Liam", "Noah", 
                    "William", "James", "Logan", "Benjamin", "Mason",
                    "Elijah", "Oliver", "Jason", "Lucas", "Michael"]

    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
                  "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", 
                  "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
                  "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", 
                  "Perez", "Thompson", "White", "Harris"]

    # Create data for the first table, account
    employee_ids = random.sample(range(1000, 2500), len(first_names))

    countries = {"USA": 1, "India": 2, "China": 3, "France": 4, "Germany": 5}
    country_names = list(countries.keys())
    country_codes = list(countries.values())
    
    departments = ["Production", "R&D", "Marketing", "HR", 
                   "Finance", "Engineering", "Managerial"]

    for f_name in first_names:
        l_name = last_names.pop()
        email = (l_name + f_name[0]).lower() + "@job.com"
        country_id = random.choice(country_codes)
        dept = random.choice(departments)
        employee_id = employee_ids.pop()
        query.addBindValue(employee_id)
        query.addBindValue(f_name)
        query.addBindValue(l_name)
        query.addBindValue(email)
        query.addBindValue(dept)
        query.addBindValue(country_id)
        query.exec()
    
    # Create data for the second table, countries
    country_query = QSqlQuery()
    country_query.exec("""CREATE TABLE countries (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                country VARCHAR(20) NOT NULL)""")

    country_query.prepare("INSERT INTO countries (country) VALUES (?)")
    
    for name in country_names:
        country_query.addBindValue(name)
        country_query.exec()

    print("[INFO] Database successfully created.")

if __name__ == "__main__":
    CreateEmployeeData()
    sys.exit(0)