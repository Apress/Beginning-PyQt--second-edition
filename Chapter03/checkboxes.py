"""Listing 3-7 to Listing 3-9
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QCheckBox, 
    QLabel)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle("QCheckBox Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        header_label = QLabel("Which shifts can you work? \
                              (Please check all that apply)", self)
        header_label.setWordWrap(True)
        header_label.move(20, 10)
        
        # Set up the checkboxes
        morning_cb = QCheckBox("Morning [8 AM-2 PM]", self) 
        morning_cb.move(40, 60)
        #morning_cb.toggle() # Uncomment to start checked
        morning_cb.toggled.connect(self.printSelected)

        after_cb = QCheckBox("Afternoon [1 PM-8 PM]", self) 
        after_cb.move(40, 80)   
        after_cb.toggled.connect(self.printSelected)

        night_cb = QCheckBox("Night [7 PM-3 AM]", self) 
        night_cb.move(40, 100)   
        night_cb.toggled.connect(self.printSelected)

    def printSelected(self, checked): 
        """Print the text of a QCheckBox object when selected
        or deselected. Use sender() to determine which widget 
        is sending the signal."""
        sender = self.sender()
        if checked:
            print(f"{sender.text()} Selected.")
        else:
            print(f"{sender.text()} Deselected.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())