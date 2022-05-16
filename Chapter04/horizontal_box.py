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
        name_edit.setClearButtonEnabled(True) #create a clear button in the right corner of the line edit widget
        name_edit.textEdited.connect(self.checkUserInput)  #connect the textEdited signal to the checkUserInput method when the user edits the text

        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.setEnabled(False) #create a disabled button when the user hasn't entered any text
        self.confirm_button.clicked.connect(self.close) #connect the clicked signal to the close method when the user clicks the button

        main_h_box = QHBoxLayout() #create a horizontal box layout
        main_h_box.addWidget(name_label) #add the name_label to the horizontal box layout
        main_h_box.addWidget(name_edit) #add the name_edit to the horizontal box layout
        main_h_box.addWidget(self.confirm_button) #add the confirm_button to the horizontal box layout 

        # Set the layout for the main window
        self.setLayout(main_h_box)  

    def checkUserInput(self, text): # text is the text that the user has entered in the line edit widget
        """Check the length and content of name_edit."""
        if len(text) > 0 \
            and all(t.isalpha() or t.isdigit() for t in text):
            self.confirm_button.setEnabled(True)
        else: self.confirm_button.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())