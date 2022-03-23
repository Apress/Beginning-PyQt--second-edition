"""Listing 6-2
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys 
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
    QVBoxLayout)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(300, 100)
        self.setWindowTitle("HTML Example")

        no_style_label = QLabel(
            """Have no fear of perfection 
            - you'll never reach it.
            - Salvador Dali""")
        style_label = QLabel("""
            <p><font color='#DB8D31' face='Times' size='+2'>
            Have no fear of perfection - 
            you'll never reach it.</font></p> 
            <p align='right'>
            <b> - <i>Salvador Dali</i></b></p>""")

        v_box = QVBoxLayout()
        v_box.addWidget(no_style_label)
        v_box.addWidget(style_label)
        self.setLayout(v_box)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())