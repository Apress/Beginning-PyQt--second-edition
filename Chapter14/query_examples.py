"""Listing 14-8 to Listing 14-10
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class QueryExamples:

    def __init__(self):
        super().__init__() 

        self.createConnection()
        self.exampleQueries()

    def createConnection(self):
        """Create connection to the database."""
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("files/accounts.db")

        if not database.open():
            print("Unable to open data source file.")
            sys.exit(1) # Error code 1 - signifies error

    def exampleQueries(self):
        """Examples of working with the database."""
        # Executing a simple query
        query = QSqlQuery()
        query.exec("SELECT first_name, last_name FROM accounts \
            WHERE employee_id > 2000")

        # The QSqlQuery constructor accepts an optional QSqlDatabase 
        # object that specifies which database connection to use. In the 
        # example above, we don't specify any connection, so the default 
        # connection is used

        # If an error occurs, exec() returns false. The error is then available 
        # as QSqlQuery::lastError()

        # Navigating the result set
        while (query.next()):
            f_name = str(query.value(0))
            l_name = str(query.value(1))
            print(f_name, l_name)

        # Inserting a single new record into the database
        query.exec("""INSERT INTO accounts (
                  employee_id, first_name, last_name, 
                  email, department, country_id) 
                  VALUES (2134, 'Robert', 'Downey', 
                    'downeyr@job.com', 'Managerial', 1)""")

        # Update a record in the database
        query.exec("UPDATE accounts SET department = 'R&D' \
            WHERE employee_id = 2134")

        # Delete a record from the database
        query.exec("DELETE FROM accounts WHERE \
            employee_id <= 1500")

if __name__ == "__main__":
    QueryExamples()
    sys.exit(0)