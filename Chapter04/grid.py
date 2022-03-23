"""Listing 4-11 to Listing 4-16
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys, json
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QLineEdit, QCheckBox, QTextEdit, QGridLayout) 
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont

class MainWindow(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(500, 300) 
        self.setWindowTitle("QGridLayout Example")

        self.setUpMainWindow()
        self.loadWidgetValuesFromFile()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        name_label = QLabel("Simple Daily Planner")
        name_label.setFont(QFont("Arial", 20))
        name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Create widgets for the left side of the window
        today_label = QLabel("• Today's Focus")
        today_label.setFont(QFont("Arial", 14))
        self.today_tedit = QTextEdit()

        notes_label = QLabel("• Notes")
        notes_label.setFont(QFont("Arial", 14))
        self.notes_tedit = QTextEdit()

        # Organize the left side widgets into a column 0
        # of the QGridLayout
        self.main_grid = QGridLayout()
        self.main_grid.addWidget(name_label, 0, 0)
        self.main_grid.addWidget(today_label, 1, 0)
        self.main_grid.addWidget(self.today_tedit, 2, 0, 3, 1)
        self.main_grid.addWidget(notes_label, 5, 0)
        self.main_grid.addWidget(self.notes_tedit, 6, 0, 3, 1)

        # Create widgets for the right side of the window
        today = QDate.currentDate().toString(Qt.DateFormat.ISODate)
        date_label = QLabel(today)
        date_label.setFont(QFont("Arial", 18))
        date_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        todo_label = QLabel("• To Do")
        todo_label.setFont(QFont("Arial", 14))

        # Organize the right side widgets into columns 1 and 2
        # of the QGridLayout
        self.main_grid.addWidget(date_label, 0, 2)
        self.main_grid.addWidget(todo_label, 1, 1, 1, 2)

        # Create 7 rows, from indexes 2-8
        for row in range(2, 9): 
            item_cb = QCheckBox()
            item_edit = QLineEdit()
            self.main_grid.addWidget(item_cb, row, 1)
            self.main_grid.addWidget(item_edit, row, 2)

        # Set the layout for the main window
        self.setLayout(self.main_grid)

    def saveWidgetValues(self):
        """Collect and save the values for the different widgets."""
        details = {"focus": self.today_tedit.toPlainText(),
                   "notes": self.notes_tedit.toPlainText()}
        remaining_todo = []

        # Check the values of the QCheckBox widgets
        for row in range(2, 9):
            # Retrieve the QLayoutItem object
            item = self.main_grid.itemAtPosition(row, 1)
            # Retrieve the widget (QCheckBox)
            widget = item.widget()
            if widget.isChecked() == False:
                # Retrieve the QLayoutItem object
                item = self.main_grid.itemAtPosition(row, 2)
                # Retrieve the widget (QLineEdit)
                widget = item.widget()
                text = widget.text()
                if text != "":
                    remaining_todo.append(text)
            # Save text from QLineEdit widgets
            details["todo"] = remaining_todo

        with open("details.txt", "w") as f:
            f.write(json.dumps(details))

    def loadWidgetValuesFromFile(self):
        """Retrieve the user's previous values from the last session."""
        # Check if file exists first
        try:
            with open("details.txt", "r") as f:
                details = json.load(f)
                # Retrieve and set values for the widgets
                self.today_tedit.setText(details["focus"])
                self.notes_tedit.setText(details["notes"])

                # Set the text for QLineEdit widgets 
                for row in range(len(details["todo"])):
                    # Retrieve the QLayoutItem object
                    item = self.main_grid.itemAtPosition(row + 2, 2)
                    # Retrieve the widget (QLineEdit)
                    widget = item.widget()
                    widget.setText(details["todo"][row])                    
        except FileNotFoundError as error:
            # Create the file since it doesn't exist
            f = open("details.txt", "w")

    def closeEvent(self, event):
        """Save widget values when closing the window."""
        self.saveWidgetValues()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())