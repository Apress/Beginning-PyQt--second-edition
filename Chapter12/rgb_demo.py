"""Listing 12-12
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
    QHBoxLayout)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from rgb_slider import RGBSlider, style_sheet

class MainWindow(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI() 

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(225, 300)
        self.setWindowTitle("12.2 - Custom Widget Example")

        # Load image
        image = QImage("images/duck_pic.png")

        # Create instance of RGB slider widget
        rgbslider = RGBSlider(image)

        image_label = QLabel()
        image_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        image_label.setPixmap(QPixmap().fromImage(image))
        # Reimplement the label's mousePressEvent
        image_label.mousePressEvent = rgbslider.getPixelValues

        h_box = QHBoxLayout()
        h_box.addWidget(rgbslider)
        h_box.addWidget(image_label)
        self.setLayout(h_box)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = MainWindow()
    sys.exit(app.exec())