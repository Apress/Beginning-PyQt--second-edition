"""Listing 4-28
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys 
from PyQt6.QtWidgets import (QApplication, QWidget,
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

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(label)
        main_v_box.addSpacing(20)
        main_v_box.addWidget(line_edit)
        main_v_box.addStretch()
        main_v_box.addWidget(button)

        self.setLayout(main_v_box)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())