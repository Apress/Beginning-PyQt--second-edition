"""Listing 10-1 to Listing 10-4
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, 
    QPushButton, QListWidget, QListWidgetItem, QInputDialog,
    QHBoxLayout, QVBoxLayout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(400, 200)
        self.setWindowTitle("QListWidget Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        self.list_widget = QListWidget()
        self.list_widget.setAlternatingRowColors(True)

        # Initialize the QListWidget with items 
        grocery_list = ["grapes", "broccoli", "garlic", "cheese",
                         "bacon", "eggs", "waffles", "rice", "soda"]
        for item in grocery_list:
            list_item = QListWidgetItem()
            list_item.setText(item)
            self.list_widget.addItem(list_item)

        # Create buttons for interacting with the items
        add_button = QPushButton("Add")
        add_button.clicked.connect(self.addListItem)

        insert_button = QPushButton("Insert")
        insert_button.clicked.connect(self.insertItemInList)

        remove_button = QPushButton("Remove")
        remove_button.clicked.connect(self.removeOneItem)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.list_widget.clear)

        # Create layouts
        right_v_box = QVBoxLayout()
        right_v_box.addWidget(add_button)
        right_v_box.addWidget(insert_button)
        right_v_box.addWidget(remove_button)
        right_v_box.addWidget(clear_button)

        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.list_widget)
        main_h_box.addLayout(right_v_box)
        self.setLayout(main_h_box)

    def addListItem(self):
        """Add a single item to the list widget."""
        text, ok = QInputDialog.getText(self, "New Item", "Add item:")
        if ok and text != "":
            list_item = QListWidgetItem()
            list_item.setText(text)
            self.list_widget.addItem(list_item)

    def insertItemInList(self):
        """Insert a single item into the list widget under 
        the currently selected row. """
        text, ok = QInputDialog.getText(self, "Insert Item", "Insert item:")
        if ok and text != "":
            row = self.list_widget.currentRow()
            row = row + 1 # Select row below current row
            new_item = QListWidgetItem()
            new_item.setText(text)
            self.list_widget.insertItem(row, new_item)

    def removeOneItem(self):
        """Remove a single item from the list widget."""
        row = self.list_widget.currentRow()
        item = self.list_widget.takeItem(row)
        del item

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())