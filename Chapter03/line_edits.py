"""Listing 3-4 to Listing 3-6
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, 
    QLabel, QLineEdit, QPushButton)
from PyQt6.QtCore import Qt

class MainWindow(QWidget): 

    def __init__(self): 
        super().__init__() 
        self.initializeUI() 

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMaximumSize(310, 130)
        self.setWindowTitle("QLineEdit Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        QLabel("Please enter your name below.",
               self).move(70, 10)
        name_label = QLabel("Name:", self)
        name_label.move(20, 50) 

        self.name_edit = QLineEdit(self)
        self.name_edit.resize(210, 20)
        self.name_edit.move(70, 50) 

        clear_button = QPushButton("Clear", self)
        clear_button.move(140, 90)
        clear_button.clicked.connect(self.clearText)

        accept_button = QPushButton("OK", self)
        accept_button.move(210, 90)        
        accept_button.clicked.connect(self.acceptText)

    def clearText(self):
        """Clear the QLineEdit input field."""
        self.name_edit.clear()

    def acceptText(self):
        """Accept the user's input in the QLineEdit
        widget and close the program."""
        print(self.name_edit.text())
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())