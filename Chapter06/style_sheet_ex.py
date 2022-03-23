"""Listing 6-3 to Listing 6-5
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(200, 200) 
        self.setWindowTitle("Style Sheets Example")                

        label = QLabel("<p align=center>Give me a like!</p>")
        label.setStyleSheet("""
            background-color: skyblue; 
            color: white; 
            border-style: outset; 
            border-width: 3px; 
            border-radius: 5px; 
            font: bold 24px 'Times New Roman'""")

        like_button = QPushButton()
        like_button.setStyleSheet(""" QPushButton {
            background-color: lightgrey; 
            padding: 5px;
            border-style: inset;
            border-width: 1px;  
            border-radius: 5px;             
            image: url(images/like_normal.png);
            qproperty-iconSize: 20px 20px;}

            QPushButton:pressed {background-color: grey;
                    padding: 5px;
                    border-style: outset; 
                    border-width: 1px; 
                    border-radius: 5px;
                    image: url(images/like_clicked.png);
                    qproperty-iconSize: 20px 20px;}""")

        v_box = QVBoxLayout()
        v_box.addWidget(label)
        v_box.addWidget(like_button)

        self.setLayout(v_box)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv) 
    window = MainWindow() 
    sys.exit(app.exec())