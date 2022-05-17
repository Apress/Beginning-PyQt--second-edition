"""Listing 4-11 to Listing 4-16
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
from base64 import encode
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

        notes_label = QLabel("• Notes")
        notes_label.setFont(QFont("Arial", 14))

        """
        The QTextEdit Widget
        When a user needs an area for entering or editing more than one line of text at a time,
        the QTextEdit class is well suited for modifying either plain or rich text and includes
        built-in editing features, such as copy, paste, and cut. The widget can handle characters
        or paragraphs of text. Paragraphs are simply long strings that are word-wrapped into the
        widget and end with a newline character. QTextEdit is also useful for displaying lists,
        images, and tables or providing an interface for displaying text using HTML.
        """

        self.today_tedit = QTextEdit() # QTextEdit is a multi-line text box 
        
        self.notes_tedit = QTextEdit() # QTextEdit is a multi-line text box . Qlabel is parent of QTextEdit

        # Organize the left side widgets into a column 0
        # of the QGridLayout
        self.main_grid = QGridLayout() # QGridLayout is a grid of widgets,it is a layout manager that organizes widgets in a grid layout row by row and column by column
        self.main_grid.setOriginCorner(Qt.Corner.TopLeftCorner) # setOriginCorner() sets the origin corner of the grid layout
        self.main_grid.addWidget(name_label, 0, 0) # addWidget(widget, row, column, rowspan, columnspan) add name label widget to grid layout at position row 0, column 0
        self.main_grid.addWidget(today_label, 1, 0) # addWidget(widget, row, column, rowspan, columnspan) add today label widget to grid layout at position row 1, column 0
        self.main_grid.addWidget(self.today_tedit, 2, 0, 3, 1) # addWidget(widget, row, column, rowspan, columnspan) add today text edit widget to grid layout at position row 2, column 0, rowspan 4, columnspan 1
        self.main_grid.addWidget(notes_label, 5, 0) # addWidget(widget, row, column, rowspan, columnspan) add notes label widget to grid layout at position row 6, column 0
        self.main_grid.addWidget(self.notes_tedit, 6, 0, 1, 1,Qt.AlignmentFlag.AlignCenter) # addWidget(widget, row, column, rowspan, columnspan,alignment) add notes text edit widget to grid layout at position row 6, column 0, rowspan 3, columnspan 1

        # Create widgets for the right side of the window
        today = QDate.currentDate().toString(Qt.DateFormat.ISODate) # QDate.currentDate() returns the current date as a QDate object and toString(Qt.DateFormat.ISODate) returns the date in ISO format
        date_label = QLabel(today) #create a label widget with the current date
        date_label.setFont(QFont("Arial", 18))
        date_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        todo_label = QLabel("• To Do") 
        todo_label.setFont(QFont("Arial", 14))

        # Organize the right side widgets into columns 1 and 2
        # of the QGridLayout
        self.main_grid.addWidget(date_label, 0, 3) # addWidget(widget, row, column, rowspan, columnspan,alignment) add date label widget to grid layout at position row 0, column 3
        self.main_grid.addWidget(todo_label, 1, 1, 1, 2) # addWidget(widget, row, column, rowspan, columnspan,alignment) add todo label widget to grid layout at position row 1, column 1, rowspan 1, columnspan 2

        # Create 7 rows, from indexes 2-8
        for row in range(2, 10): 
            item_cb = QCheckBox(f"check{row-1}") #create a checkbox widget 
            item_edit = QLineEdit() #create a line edit widget
            item_edit.setPlaceholderText("Enter item here") #set the placeholder text of the line edit widget
            self.main_grid.addWidget(item_cb, row, 1) # addWidget(widget, row, column, rowspan, columnspan,alignment) add checkbox widget to grid layout at position row 2, column 1
            self.main_grid.addWidget(item_edit, row, 2) # addWidget(widget, row, column, rowspan, columnspan,alignment) add line edit widget to grid layout at position row 2, column 2

        # Set the layout for the main window
        self.setLayout(self.main_grid)

    def saveWidgetValues(self):
        """Collect and save the values for the different widgets."""
        details = {"focus": self.today_tedit.toPlainText(),
                   "notes": self.notes_tedit.toPlainText()} # toPlainText() returns the text of the widget as a plain text string
        remaining_todo = []

        # Check the values of the QCheckBox widgets
        for row in range(2, 9):
            # Retrieve the QLayoutItem object
            item = self.main_grid.itemAtPosition(row, 1) # itemAtPosition(row, column) returns the QLayoutItem object at the given row and column 1 of the grid layout
            # Retrieve the widget (QCheckBox)
            widget = item.widget() # widget() returns the checkbox widget that is managed by the layout item
            if widget.isChecked() == False:
                # Retrieve the QLayoutItem object
                item = self.main_grid.itemAtPosition(row, 2)  # returns the QLayoutItem object at the given row and column 2 of the grid layout
                # Retrieve the widget (QLineEdit)
                widget = item.widget() # widget() returns the Qlineedit that is managed by the layout item
                text = widget.text() # text() returns the text of the qlineedit widget
                if text != "":
                    remaining_todo.append(text) #append the text of the qlineedit widget to the remaining_todo list
            # Save text from QLineEdit widgets
            details["todo"] = remaining_todo # set the to_do key , value is the remaining_todo list

        with open("details.txt", "w") as f: # open the details.txt file in write mode and store the file object in f variable
            print(f"Saving details to file: {details}")
            print(json.dumps(details,))
            f.write(json.dumps(details)) # write the json.dumps(details) to the details.txt file , json.dumps() returns a string containing the JSON representation of the object passed as an argument to it

    def loadWidgetValuesFromFile(self):
        """Retrieve the user's previous values from the last session."""
        # Check if file exists first
        try:
            with open("details.txt", "r") as f: # open the details.txt file in read mode and store the file object in f variable
                details = json.load(f) # load the json.load(f) from the details.txt file , json.load() returns the Python object that was serialized as a JSON string
                # Retrieve and set values for the widgets
                self.today_tedit.setText(details["focus"]) # set the text of the today text edit widget to the value of the focus key
                self.notes_tedit.setText(details["notes"]) # set the text of the notes text edit widget to the value of the notes key

                # Set the text for QLineEdit widgets 
                for row in range(len(details["todo"])): # for each item in the todo list
                    # Retrieve the QLayoutItem object
                    item = self.main_grid.itemAtPosition(row + 2, 2) # returns the today_edit widget at the given row and column 2 of the grid layout
                    # Retrieve the widget (QLineEdit)
                    widget = item.widget() # widget() returns the Qlineedit that is managed by the layout item
                    widget.setText(details["todo"][row]) # set the text of the today_edit Qlineedit widget to the value of the todo key
        except FileNotFoundError as error:
            # Create the file since it doesn't exist
            with open("./details.txt", "w") as f: # open the details.txt file in write mode and store the file object in f variable
                pass

    def closeEvent(self, event):
        """Save widget values when closing the window."""
        self.saveWidgetValues()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())