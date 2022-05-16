"""Listing 4-7 to Listing 4-10
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
    QComboBox, QSpinBox, QHBoxLayout, QVBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MainWindow(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(400, 160) 
        self.setWindowTitle('Nested Layout Example')

        self.setUpMainWindow() # Create and arrange widgets in the main window
        self.show() # Display the main window

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        info_label = QLabel(
            "Select 2 items for lunch and their prices.")
        info_label.setFont(QFont("Arial", 16))
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a list of food items and two separate 
        # QComboBox widgets to display all of the items
        food_list = ["egg", "turkey sandwich", "ham sandwich",
            "cheese", "hummus", "yogurt", "apple", "banana", 
            "orange", "waffle", "carrots", "bread", "pasta", 
            "crackers", "pretzels", "coffee", "soda", "water"]

        food_combo1 = QComboBox() # Create the first QComboBox widget like Dropdown list
        food_combo1.addItems(food_list) # Add the food items to the dropdown list
        food_combo2 = QComboBox()
        food_combo2.addItems(food_list)

        # Create two QSpinBox widgets to display prices
        self.price_sb1 = QSpinBox() # Create the first QSpinBox widget.spinbox allows the user to enter a number in a text box and the user can click the up and down arrows to increase or decrease the number
        self.price_sb1.setRange(0, 100) # Set the range of the spinbox
        self.price_sb1.setPrefix("$") #set the prefix of the spinbox, which is the currency symbol of the country
        self.price_sb1.valueChanged.connect(self.calculateTotal) # Connect the spinbox to the calculateTotal function so that when the value of the spinbox changes, the calculateTotal function is called

        self.price_sb2 = QSpinBox()
        self.price_sb2.setRange(0, 100)
        self.price_sb2.setPrefix("$")
        self.price_sb2.valueChanged.connect(self.calculateTotal)

        # Create two horizontal layouts for the QComboBox 
        # and QSpinBox widgets
        item1_h_box = QHBoxLayout()
        item1_h_box.addWidget(food_combo1)
        item1_h_box.addWidget(self.price_sb1)

        item2_h_box = QHBoxLayout()
        item2_h_box.addWidget(food_combo2)
        item2_h_box.addWidget(self.price_sb2)        

        self.totals_label = QLabel("Total Spent: $") # Create a label to display the total price
        self.totals_label.setFont(QFont("Arial", 16)) # Set the font of the label
        self.totals_label.setAlignment(Qt.AlignmentFlag.AlignRight) # Set the alignment of the label to the right

        # Organize widgets and layouts in the main window
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(info_label)
        main_v_box.addLayout(item1_h_box)
        main_v_box.addLayout(item2_h_box)
        main_v_box.addWidget(self.totals_label)

        # Set the layout for the main window
        self.setLayout(main_v_box)

    def calculateTotal(self, value):
        """Calculate the total price and update 
        totals_label."""
        total = self.price_sb1.value() + self.price_sb2.value() # Calculate the total price of the two spinboxes values
        self.totals_label.setText(f"Total Spent: ${total}") # Update the totals_label with the total price

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())