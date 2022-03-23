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

        self.setUpMainWindow()
        self.show()

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

        food_combo1 = QComboBox()
        food_combo1.addItems(food_list)
        food_combo2 = QComboBox()
        food_combo2.addItems(food_list)

        # Create two QSpinBox widgets to display prices
        self.price_sb1 = QSpinBox()
        self.price_sb1.setRange(0, 100)
        self.price_sb1.setPrefix("$")
        self.price_sb1.valueChanged.connect(self.calculateTotal)

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

        self.totals_label = QLabel("Total Spent: $")
        self.totals_label.setFont(QFont("Arial", 16))
        self.totals_label.setAlignment(Qt.AlignmentFlag.AlignRight)

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
        total = self.price_sb1.value() + \
            self.price_sb2.value()
        self.totals_label.setText(f"Total Spent: ${total}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())