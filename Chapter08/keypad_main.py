"""Listing 8-11 to Listing 8-15
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from keypad_gui import Ui_Keypad

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Keypad()
        self.ui.setupUi(self)

        self.initializeUI()
        self.show()

    def initializeUI(self):
        """Set up the application's GUI."""
        # Update other line_edit features
        self.ui.line_edit1.setMaxLength(1) # Set the max number of characters allowed
        self.ui.line_edit1.setValidator(QIntValidator(0, 9)) # User can only enter ints from 0-9
        self.ui.line_edit1.setFocusPolicy(Qt.FocusPolicy.NoFocus) # Widget does not except focus

        self.ui.line_edit2.setMaxLength(1) 
        self.ui.line_edit2.setValidator(QIntValidator(0, 9)) 
        self.ui.line_edit2.setFocusPolicy(Qt.FocusPolicy.NoFocus) 

        self.ui.line_edit3.setMaxLength(1) 
        self.ui.line_edit3.setValidator(QIntValidator(0, 9)) 
        self.ui.line_edit3.setFocusPolicy(Qt.FocusPolicy.NoFocus) 

        self.ui.line_edit4.setMaxLength(1) 
        self.ui.line_edit4.setValidator(QIntValidator(0, 9)) 
        self.ui.line_edit4.setFocusPolicy(Qt.FocusPolicy.NoFocus) 

        # 4-digit passcode
        self.passcode = 8618
        
        # Add signal/slot connections for buttons
        self.ui.button_0.clicked.connect(lambda: self.numberClicked(self.ui.button_0.text()))
        self.ui.button_1.clicked.connect(lambda: self.numberClicked(self.ui.button_1.text()))
        self.ui.button_2.clicked.connect(lambda: self.numberClicked(self.ui.button_2.text()))
        self.ui.button_3.clicked.connect(lambda: self.numberClicked(self.ui.button_3.text()))
        self.ui.button_4.clicked.connect(lambda: self.numberClicked(self.ui.button_4.text()))
        self.ui.button_5.clicked.connect(lambda: self.numberClicked(self.ui.button_5.text()))
        self.ui.button_6.clicked.connect(lambda: self.numberClicked(self.ui.button_6.text()))
        self.ui.button_7.clicked.connect(lambda: self.numberClicked(self.ui.button_7.text()))
        self.ui.button_8.clicked.connect(lambda: self.numberClicked(self.ui.button_8.text()))
        self.ui.button_9.clicked.connect(lambda: self.numberClicked(self.ui.button_9.text()))

        self.ui.button_hash.clicked.connect(self.checkPasscode)

    def numberClicked(self, text_value):
        """When a button with a digit is pressed, check if 
        the text for QLineEdit widgets are empty. If empty, 
        set the focus to the correct widget and enter text value."""
        if self.ui.line_edit1.text() == "":
            self.ui.line_edit1.setFocus()
            self.ui.line_edit1.setText(text_value)
            self.ui.line_edit1.repaint()
        elif (self.ui.line_edit1.text() != "") and (self.ui.line_edit2.text() == ""):
            self.ui.line_edit2.setFocus()
            self.ui.line_edit2.setText(text_value)
            self.ui.line_edit2.repaint()
        elif (self.ui.line_edit1.text() != "") and (self.ui.line_edit2.text() != "") \
            and (self.ui.line_edit3.text() == ""):
            self.ui.line_edit3.setFocus()
            self.ui.line_edit3.setText(text_value)
            self.ui.line_edit3.repaint()
        elif (self.ui.line_edit1.text() != "") and (self.ui.line_edit2.text() != "") \
            and (self.ui.line_edit3.text() != "") and (self.ui.line_edit4.text() == ""):
            self.ui.line_edit4.setFocus()
            self.ui.line_edit4.setText(text_value)
            self.ui.line_edit4.repaint()
        
    def checkPasscode(self):
        """Concatenate the text values from the 4 QLineEdit widgets,
        and check to see if the passcode entered by user matches 
        existing passcode."""
        entered_passcode = self.ui.line_edit1.text() + self.ui.line_edit2.text() + \
            self.ui.line_edit3.text() +  self.ui.line_edit4.text()
        if len(entered_passcode) == 4 and int(entered_passcode) == self.passcode:
            QMessageBox.information(self, "Valid Passcode!", "Valid Passcode!", 
                QMessageBox.StandardButton.Ok)
            self.close()
        else:
            QMessageBox.warning(self, "Error Message", "Invalid Passcode.", 
                QMessageBox.StandardButton.Close)
            self.ui.line_edit1.clear()
            self.ui.line_edit2.clear()
            self.ui.line_edit3.clear()
            self.ui.line_edit4.clear()
            self.ui.line_edit1.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Keypad = MainWindow()
    sys.exit(app.exec())