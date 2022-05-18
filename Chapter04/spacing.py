"""Listing 4-28
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys 
from PyQt6.QtWidgets import (QApplication, QWidget,QSizePolicy,
    QLabel, QPushButton, QLineEdit, QVBoxLayout)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(300, 200)
        self.setWindowTitle("Spacing Example")

        label = QLabel("Enter text")
        line_edit = QLineEdit()
         
        button = QPushButton("End")
        button.sizeHint() #set the button's size to be the same as the button's text (i.e. the button's text will be the same size as the button)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(label)
        main_v_box.addSpacing(20) #add a vertical spacing of 20 pixels between the label and the line edit
        main_v_box.addWidget(line_edit)
        main_v_box.addStretch() #add a stretch to the layout to make the line edit stretch to fill the remaining space
        main_v_box.addWidget(button)
        main_v_box.setContentsMargins(10, 20,30,40) #sets the contents margins to 10 pixels on the left, 20 pixels on the top, 30 pixels on the right, and 40 pixels on the bottom



        self.setLayout(main_v_box)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())