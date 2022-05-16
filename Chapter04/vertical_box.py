"""Listing 4-4 to Listing 4-6
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
    QCheckBox, QPushButton, QButtonGroup, QVBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MainWindow(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(350, 200) 
        self.setWindowTitle("QVBoxLayout Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        header_label = QLabel("Chez PyQt6")
        header_label.setFont(QFont("Arial", 18))
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        question_label = QLabel(
            "How would you rate your service?")
        question_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        ratings = ["Satisfied", "Average", "Not Satisfied"]   
        # Create a QButtonGroup object for the ratings checkboxes
        ratings_group = QButtonGroup(self)  
        ratings_group.buttonClicked.connect(self.checkboxClicked) # Connect the buttonClicked signal to the checkboxClicked method                

        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.setEnabled(False)  # Disable the confirm button until a checkbox is clicked
        self.confirm_button.clicked.connect(self.close) # Connect the clicked signal to the close method

        # Organize the widgets into a layout
        main_v_box = QVBoxLayout() # Create a QVBoxLayout main object
        main_v_box.addWidget(header_label) # Add the header_label to the main layout
        main_v_box.addWidget(question_label) # Add the question_label to the main layout

        # Create the QCheckBox objects, then add 
        # them to the QButtonGroup and the main layout
        for cb in range(len(ratings)):
            rating_cb = QCheckBox(ratings[cb]) #create a checkbox for each rating in the ratings list
            ratings_group.addButton(rating_cb) #add the checkbox to the button group
            main_v_box.addWidget(rating_cb) #add the checkbox to the main layout

        main_v_box.addWidget(self.confirm_button) #add the confirm_button to the main layout

        # Set the layout for the main window
        self.setLayout(main_v_box) 

    def checkboxClicked(self, button): # button is the checkbox that was clicked
        """Check if a QCheckBox in the QButtonGroup has
        been clicked."""
        print(button.text())
        self.confirm_button.setEnabled(True) #enable the confirm_button

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())