"""Listing 16-7
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys 
from PyQt6.QtWidgets import (QApplication, QWidget, 
    QCheckBox, QGroupBox, QButtonGroup, QVBoxLayout)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(300, 200)
        self.setWindowTitle("Tri-State Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        self.tristate_cb = QCheckBox("Select all toppings")
        self.tristate_cb.stateChanged.connect(self.updateTristateCb)

        # Create the check boxes with an indentation
        # using style sheets
        topping1_cb = QCheckBox("Chocolate Chips")
        topping1_cb.setStyleSheet("padding-left: 20px")
        topping2_cb = QCheckBox("Gummy Bears")
        topping2_cb.setStyleSheet("padding-left: 20px")
        topping3_cb = QCheckBox("Oreos, Peanuts")
        topping3_cb.setStyleSheet("padding-left: 20px")

        # Create a non-exclusive group of check boxes
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(False)
        self.button_group.addButton(topping1_cb)
        self.button_group.addButton(topping2_cb)
        self.button_group.addButton(topping3_cb)
        self.button_group.buttonToggled.connect(self.checkButtonState)

        gb_v_box = QVBoxLayout()
        gb_v_box.addWidget(self.tristate_cb)
        gb_v_box.addWidget(topping1_cb)
        gb_v_box.addWidget(topping2_cb)
        gb_v_box.addWidget(topping3_cb)
        gb_v_box.addStretch()

        group_box = QGroupBox("Choose the toppings for your ice cream")
        group_box.setLayout(gb_v_box)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(group_box)
        self.setLayout(main_v_box)

    def updateTristateCb(self, state):
        """Use the QCheckBox to check or uncheck all boxes."""
        for button in self.button_group.buttons():
            if state == 2: # Qt.CheckState.Checked
                button.setChecked(True)
            elif state == 0: # Qt.CheckState.Unchecked
                button.setChecked(False)
    
    def checkButtonState(self, button, checked):
        """Determine which buttons are selected and set the state
        of the tri-state QCheckBox."""
        button_states = []

        for button in self.button_group.buttons():
            button_states.append(button.isChecked())

        if all(button_states):
            self.tristate_cb.setCheckState(Qt.CheckState.Checked)
            self.tristate_cb.setTristate(False)
        elif any(button_states) == False:
            self.tristate_cb.setCheckState(Qt.CheckState.Unchecked)
            self.tristate_cb.setTristate(False)
        else:
            self.tristate_cb.setCheckState(Qt.CheckState.PartiallyChecked)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())