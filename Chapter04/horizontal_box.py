"""Listing 4-1 to Listing 4-3
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys 
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
    QLineEdit, QPushButton, QHBoxLayout)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumWidth(500)
        self.setFixedHeight(60)
        self.setWindowTitle('QHBoxLayout Example')

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        name_label = QLabel("New Username:")

        name_edit = QLineEdit()
        name_edit.setClearButtonEnabled(True)
        name_edit.textEdited.connect(self.checkUserInput)

        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.setEnabled(False)
        self.confirm_button.clicked.connect(self.close)

        main_h_box = QHBoxLayout()
        main_h_box.addWidget(name_label)
        main_h_box.addWidget(name_edit)
        main_h_box.addWidget(self.confirm_button)

        # Set the layout for the main window
        self.setLayout(main_h_box)

    def checkUserInput(self, text):
        """Check the length and content of name_edit."""
        if len(text) > 0 \
            and all(t.isalpha() or t.isdigit() for t in text):
            self.confirm_button.setEnabled(True)
        else: self.confirm_button.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())