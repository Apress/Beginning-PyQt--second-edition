"""Listing 10-5 to Listing 10-6
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys, os
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QListWidget, QListWidgetItem, QGridLayout)
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(500, 300)
        self.setWindowTitle("Drag and Drop Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        icon_label = QLabel("ICONS", self)
        icon_widget = QListWidget()
        icon_widget.setAcceptDrops(True)
        icon_widget.setDragEnabled(True)
        icon_widget.setViewMode(
            QListWidget.ViewMode.IconMode)

        image_path = "images"   
        for img in os.listdir(image_path):
            list_item = QListWidgetItem()
            list_item.setText(img.split(".")[0])
            list_item.setIcon(QIcon(os.path.join(image_path, 
                                "{0}").format(img)))
            icon_widget.setIconSize(QSize(50, 50))
            icon_widget.addItem(list_item)

        list_label = QLabel("LIST", self)
        list_widget = QListWidget()
        list_widget.setAlternatingRowColors(True)
        list_widget.setAcceptDrops(True)
        list_widget.setDragEnabled(True)

        # create grid layout
        grid = QGridLayout()
        grid.addWidget(icon_label, 0, 0)
        grid.addWidget(list_label, 0, 1)
        grid.addWidget(icon_widget, 1, 0)
        grid.addWidget(list_widget, 1, 1)

        self.setLayout(grid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())