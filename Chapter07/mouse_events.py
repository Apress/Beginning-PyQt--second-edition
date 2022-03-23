"""Listing 7-2 to Listing 7-4
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QVBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI() 

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(400, 300)
        self.setWindowTitle("Event Handling Example")
        #self.setMouseTracking(True)

        self.setUpMainWindow()        
        self.show()

    def setUpMainWindow(self):
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap("images/back.png"))
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.info_label = QLabel("") 
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.pos_label = QLabel("")
        self.pos_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_h_box = QVBoxLayout()
        main_h_box.addStretch()
        main_h_box.addWidget(self.image_label)
        main_h_box.addStretch()
        main_h_box.addWidget(self.info_label)
        main_h_box.addWidget(self.pos_label)
        self.setLayout(main_h_box)

    def enterEvent(self, event):
        self.image_label.setPixmap(QPixmap("images/front.png"))

    def leaveEvent(self, event):
        self.image_label.setPixmap(QPixmap("images/back.png"))

    def mouseMoveEvent(self, event):
        """Print the mouse position while clicked and moving."""
        if self.underMouse():
            self.pos_label.setText(
                f"""<p>X:{event.position().x()},
                    Y:{event.position().y()}</p>""")

    def mousePressEvent(self, event):
        """Determine which button was clicked."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.info_label.setText("<b>Left Click</b>")
        if event.button() == Qt.MouseButton.RightButton:
            self.info_label.setText("<b>Right Click</b>")
        
    def mouseReleaseEvent(self, event):
        """Determine which button was released."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.info_label.setText("<b>Left Button Released</b>")
        if event.button() == Qt.MouseButton.RightButton:
            self.info_label.setText("<b>Right Button Released</b>")

    def mouseDoubleClickEvent(self, event):
        self.image_label.setPixmap(QPixmap("images/boom.png"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())