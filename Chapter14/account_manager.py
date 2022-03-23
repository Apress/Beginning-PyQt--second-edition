"""Listing 14-18 to Listing 14-24
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys, os
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QPushButton, QComboBox, QTableView, QHeaderView, 
    QAbstractItemView, QMessageBox, QHBoxLayout, QVBoxLayout, 
    QSizePolicy)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtSql import (QSqlDatabase, QSqlQuery, QSqlRelation, 
    QSqlRelationalTableModel, QSqlRelationalDelegate)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI() 

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(1000, 600)
        self.setWindowTitle("14.1 – Account Management GUI")

        self.createConnection()
        self.createModel()
        self.setUpMainWindow()
        self.show()

    def createConnection(self):
        """Set up the connection to the database.
        Check for the tables needed."""
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("files/accounts.db")

        if not database.open():
            print("Unable to open data source file.")
            sys.exit(1) # Error code 1 - signifies error

        # Check if the tables we need exist in the database
        tables_needed = {"accounts", "countries"}
        tables_not_found = tables_needed - set(database.tables())
        if tables_not_found:
            QMessageBox.critical(None, "Error",
                f"""<p>The following tables are missing 
                from the database: {tables_not_found}</p>""")
            sys.exit(1) # Error code 1 - signifies error

    def createModel(self):
        """Set up the model and headers, and populate the model."""
        self.model = QSqlRelationalTableModel()
        self.model.setTable("accounts")
        self.model.setRelation(self.model.fieldIndex("country_id"), QSqlRelation("countries", "id", "country"))

        self.model.setHeaderData(self.model.fieldIndex("id"), Qt.Orientation.Horizontal, "ID")
        self.model.setHeaderData(self.model.fieldIndex("employee_id"), Qt.Orientation.Horizontal, "Employee ID")
        self.model.setHeaderData(self.model.fieldIndex("first_name"), Qt.Orientation.Horizontal, "First")
        self.model.setHeaderData(self.model.fieldIndex("last_name"), Qt.Orientation.Horizontal, "Last")
        self.model.setHeaderData(self.model.fieldIndex("email"), Qt.Orientation.Horizontal, "E-mail")
        self.model.setHeaderData(self.model.fieldIndex("department"), Qt.Orientation.Horizontal, "Dept.")
        self.model.setHeaderData(self.model.fieldIndex("country_id"), Qt.Orientation.Horizontal, "Country")
        
        # Populate the model with data
        self.model.select()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        icons_path = "icons"

        title = QLabel("Account Management System")
        title.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        title.setStyleSheet("font: bold 24px")

        add_product_button = QPushButton("Add Employee")
        add_product_button.setIcon(QIcon(os.path.join(icons_path, "add_user.png")))
        add_product_button.setStyleSheet("padding: 10px")
        add_product_button.clicked.connect(self.addItem)

        del_product_button = QPushButton("Delete")
        del_product_button.setIcon(QIcon(os.path.join(icons_path, "trash_can.png")))
        del_product_button.setStyleSheet("padding: 10px")
        del_product_button.clicked.connect(self.deleteItem)

        # Set up sorting combobox
        sorting_options = ["Sort by ID", "Sort by Employee ID", 
                           "Sort by First Name", "Sort by Last Name", 
                           "Sort by Department", "Sort by Country"]
        sort_combo = QComboBox()
        sort_combo.addItems(sorting_options)
        sort_combo.currentTextChanged.connect(self.setSortingOrder)

        buttons_h_box = QHBoxLayout()
        buttons_h_box.addWidget(add_product_button)
        buttons_h_box.addWidget(del_product_button)
        buttons_h_box.addStretch()
        buttons_h_box.addWidget(sort_combo)

        # Widget to contain editing buttons
        edit_container = QWidget()
        edit_container.setLayout(buttons_h_box)

        # Create table view and set model 
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        horizontal = self.table_view.horizontalHeader()
        horizontal.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        vertical = self.table_view.verticalHeader()
        vertical.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.table_view.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        # Instantiate the delegate
        delegate = QSqlRelationalDelegate()
        self.table_view.setItemDelegate(delegate)

        # Main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(title, Qt.AlignmentFlag.AlignLeft)
        main_v_box.addWidget(edit_container)
        main_v_box.addWidget(self.table_view)
        self.setLayout(main_v_box)

    def addItem(self):
        """Add a new record to the last row of the table."""
        last_row = self.model.rowCount()
        self.model.insertRow(last_row)

        query = QSqlQuery()
        query.exec("SELECT MAX (id) FROM accounts")
        if query.next():
            int(query.value(0))

    def deleteItem(self):
        """Delete an entire row from the table."""
        current_item = self.table_view.selectedIndexes()
        for index in current_item:
            self.model.removeRow(index.row())
        self.model.select()

    def setSortingOrder(self, text):
        """Sort the rows in the table."""
        if text == "Sort by ID":
            self.model.setSort(self.model.fieldIndex("id"), Qt.SortOrder.AscendingOrder)
        elif text == "Sort by Employee ID":
            self.model.setSort(self.model.fieldIndex("employee_id"), Qt.SortOrder.AscendingOrder)
        elif text == "Sort by First Name":
            self.model.setSort(self.model.fieldIndex("first_name"), Qt.SortOrder.AscendingOrder)
        elif text == "Sort by Last Name":
            self.model.setSort(self.model.fieldIndex("last_name"), Qt.SortOrder.AscendingOrder)
        elif text == "Sort by Department":
            self.model.setSort(self.model.fieldIndex("department"), Qt.SortOrder.AscendingOrder)
        elif text == "Sort by Country":
            self.model.setSort(self.model.fieldIndex("country"), Qt.SortOrder.AscendingOrder)

        self.model.select()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())