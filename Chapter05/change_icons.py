"""Listing 5-3 to Listing 5-6
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
    QLabel, QPushButton, QVBoxLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(200, 200) 
        self.setWindowTitle("Changing Icons Example")
        self.setWindowIcon(QIcon("images/pyqt_logo.png"))

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        info_label = QLabel("Click on the button and select a fruit.") 
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.images = [
            "images/1_apple.png", "images/2_pineapple.png",
            "images/3_watermelon.png", "images/4_banana.png"]

        self.icon_button = QPushButton()
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))
        self.icon_button.clicked.connect(self.changeButtonIcon)

        # Create vertical layout and add widgets
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(info_label)
        main_v_box.addWidget(self.icon_button)

        # Set main layout of window
        container = QWidget()
        container.setLayout(main_v_box)
        self.setCentralWidget(container)

    def changeButtonIcon(self):
        """When the button is clicked, change the icon to 
        a different random icon from the images list."""
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))

if __name__ == '__main__':
    app = QApplication(sys.argv) 
    window = MainWindow() 
    sys.exit(app.exec())